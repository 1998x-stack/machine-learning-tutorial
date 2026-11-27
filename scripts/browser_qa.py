#!/usr/bin/env python3
"""Capture and assert responsive local-file rendering at 1440, 390 and 360 px."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'reports' / 'browser-qa'
FILES = [ROOT / 'docs' / 'index.html'] + [
    ROOT / 'docs' / 'chapters' / f'{i:02}.html' for i in range(1, 29)
]
VIEWPORTS = [('desktop', 1440, 900), ('mobile', 390, 844), ('compact', 360, 780)]

def main():
    failures = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for name, width, height in VIEWPORTS:
            for path in FILES:
                page = browser.new_page(viewport={'width': width, 'height': height},
                                        device_scale_factor=1)
                errors = []
                page.on('pageerror', lambda e: errors.append(str(e)))
                page.goto(path.as_uri(), wait_until='load')
                # Lazy-loaded below-the-fold SVGs must be decoded before
                # classifying them as broken at a mobile-sized viewport.
                page.evaluate("""async () => {
                  const images = Array.from(document.images);
                  images.forEach(img => { img.loading = 'eager'; });
                  await Promise.all(images.map(img => img.decode().catch(() => null)));
                }""")
                result = page.evaluate('''() => ({
                  scroll: document.documentElement.scrollWidth,
                  viewport: innerWidth,
                  h1: document.querySelectorAll('h1').length,
                  brokenImages: [...document.images].filter(x => !x.complete || x.naturalWidth===0).map(x=>x.src),
                  mathCount: document.querySelectorAll('math').length
                })''')
                if result['scroll'] > width + 1:
                    failures.append(f'{name} {path.name}: horizontal overflow {result["scroll"]}>{width}')
                if result['h1'] != 1:
                    failures.append(f'{name} {path.name}: h1 count {result["h1"]}')
                if result['brokenImages']:
                    failures.append(f'{name} {path.name}: broken image(s) {result["brokenImages"]}')
                if path.name != 'index.html':
                    if result['mathCount'] == 0:
                        failures.append(f'{name} {path.name}: missing MathML')
                    else:
                        bb = page.locator('math').first.bounding_box()
                        if not bb or bb['height'] < 5:
                            failures.append(f'{name} {path.name}: MathML has no visible geometry')
                if errors:
                    failures.extend(f'{name} {path.name}: {msg}' for msg in errors)
                dest = OUT / name
                dest.mkdir(parents=True, exist_ok=True)
                page.screenshot(path=str(dest / (path.stem + '.png')), animations='disabled')
                if path.name == '07.html':
                    slider = page.locator('#threshold-07')
                    if slider.count() != 1:
                        failures.append(f'{name} 07: threshold control missing')
                    else:
                        initial_tp = page.locator('[data-field="tp"]').inner_text()
                        initial_tn = page.locator('[data-field="tn"]').inner_text()
                        if initial_tp != '2' or initial_tn != '3':
                            failures.append(f'{name} 07: default counts incorrect')
                        slider.evaluate("""el => {
                          el.value = '0.75';
                          el.dispatchEvent(new Event('input', {bubbles:true}));
                        }""")
                        tp = page.locator('[data-field="tp"]').inner_text()
                        tn = page.locator('[data-field="tn"]').inner_text()
                        if tp != '1' or tn != '4':
                            failures.append(f'{name} 07: slider counts incorrect')
                if path.name == 'index.html':
                    page.locator('#course-search').fill('梯度')
                    visible = page.locator('.lesson-card:not([hidden])')
                    if visible.count() != 1 or '04.html' not in visible.first.get_attribute('href'):
                        failures.append(f'{name} home: search for gradient did not filter to chapter 04')
                print(f'{name}: {path.relative_to(ROOT)} (scroll {result["scroll"]}, MathML {result["mathCount"]})')
                page.close()
        browser.close()
    if failures:
        print('\n'.join('ERROR ' + x for x in failures))
        return 1
    print('PASS 87 viewport-page checks, three search interactions, MathML geometry and SVG images')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
