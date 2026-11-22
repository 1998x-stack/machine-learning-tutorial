(function () {
  "use strict";
  document.querySelectorAll(".threshold-lab").forEach(function (root) {
    const labels = root.dataset.labels.split(",").map(Number);
    const scores = root.dataset.scores.split(",").map(Number);
    const slider = root.querySelector('input[type="range"]');
    const value = root.querySelector(".lab-value");
    if (!slider || !value || labels.length !== scores.length ||
        !labels.length || labels.some(x => x !== 0 && x !== 1) ||
        scores.some(x => !Number.isFinite(x))) return;
    function display() {
      const cutoff = Number(slider.value);
      let tp=0, fp=0, fn=0, tn=0;
      labels.forEach(function (truth, i) {
        const positive = scores[i] >= cutoff - 1e-10;
        if (truth === 1 && positive) tp++;
        else if (truth === 1) fn++;
        else if (positive) fp++;
        else tn++;
      });
      const values = {tp, fp, fn, tn,
        precision: tp+fp === 0 ? "N/A" : (tp/(tp+fp)).toFixed(2),
        recall: tp+fn === 0 ? "N/A" : (tp/(tp+fn)).toFixed(2)};
      value.textContent = cutoff.toFixed(2);
      slider.setAttribute("aria-valuetext", cutoff.toFixed(2));
      root.querySelectorAll("[data-field]").forEach(function (element) {
        const field = element.dataset.field;
        if (Object.prototype.hasOwnProperty.call(values, field)) {
          element.textContent = String(values[field]);
        }
      });
    }
    slider.addEventListener("input", display);
    display();
  });
})();
