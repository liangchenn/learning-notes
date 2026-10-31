# STAT 581: Advanced Statistical Theory

English edited notes with corrected derivations, resolved handwritten TODOs, and labeled lecture supplements.

| Volume | PDF | Editable source |
|---|---|---|
| 1: Decision Theory and Bayesian Inference | [PDF](stat581-note1.pdf) | — |
| 2: Admissibility and Stein’s Phenomenon | [PDF](stat581-note2.pdf) | — |
| 3: Large Sample Theory and Distributional Distances | [PDF](stat581-note3.pdf) | [LaTeX](stat581-note3.tex) |
| 4: M-estimation and Maximum Likelihood | [PDF](stat581-note4.pdf) | [LaTeX](stat581-note4.tex) |

Updated October 30, 2026: Note 3 integrates the October 28 ratio-estimator continuation; Note 4 integrates the October 28 handwritten score/Taylor/sandwich derivation while retaining earlier Lecture 3 complements. [Source coverage and corrections](SOURCE-MAP.md).

Yellow boxes preserve and answer TODOs; red boxes explain corrections; blue boxes add concepts; gray boxes explain remarks. Cyan boxes in Note 3 record material recovered during the earlier teacher-source comparison. The seven distance diagrams are embedded vector TikZ figures.

## Rebuild Notes 3 and 4

Requires XeLaTeX (MacTeX/TeX Live), New Computer Modern fonts, `unicode-math`, `tcolorbox`, and TikZ. Both sources are self-contained; no external figure files or source PDFs are needed to compile.

```sh
mkdir -p build
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build stat581-note3.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build stat581-note3.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build stat581-note4.tex
xelatex -interaction=nonstopmode -halt-on-error -output-directory=build stat581-note4.tex
```

Repeat if the compiler requests another pass for the table of contents or references. PDFs are written into `build/`. All formulas use `equation`, `align`, or their contained structures; there is no inline math or bracket-delimited display math.

The handwritten source filenames inside the documents identify provenance; their original relative paths refer to the course workspace and are not required dependencies here. Historical exam-scope comments do not establish current exam coverage.
