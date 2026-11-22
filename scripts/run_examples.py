#!/usr/bin/env python3
"""Execute the Python blocks embedded in chapters 01–28 as independent examples."""
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
class Extractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_pre = False
        self.in_code = False
        self.code = []
        self.blocks = []
    def handle_starttag(self, tag, attrs):
        if tag == 'pre':
            self.in_pre = True
        elif tag == 'code' and self.in_pre:
            self.in_code = True
            self.code = []
    def handle_data(self, data):
        if self.in_code:
            self.code.append(data)
    def handle_endtag(self, tag):
        if tag == 'code' and self.in_code:
            self.in_code = False
            self.blocks.append(''.join(self.code))
        elif tag == 'pre':
            self.in_pre = False

def main():
    total = 0
    for i in range(1, 29):
        path = ROOT / 'docs' / 'chapters' / f'{i:02}.html'
        parser = Extractor()
        parser.feed(path.read_text(encoding='utf-8'))
        if not parser.blocks:
            raise AssertionError(f'{path.name}: no runnable Python examples')
        for j, code in enumerate(parser.blocks, 1):
            result = subprocess.run(
                [sys.executable, '-c', code], text=True, capture_output=True,
                timeout=90, cwd=ROOT,
            )
            if result.returncode:
                print(f'FAIL {path.name} example {j}: {result.stderr}\n{result.stdout}')
                return 1
            print(f'PASS {path.name} example {j}: {result.stdout.strip()[:180]}')
            total += 1
    print(f'PASS {total} independent Python examples')
    return 0

if __name__ == '__main__':
    sys.exit(main())
