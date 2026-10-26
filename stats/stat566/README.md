# STAT 566: Causal Modeling

English, mathematically edited notes transcribed from Liang-Cheng Chen's four handwritten course PDFs, checked against Ema Perković's Spring 2026 lecture notes.

| Volume | Subject | Handwritten source |
|---|---|---|
| [Combined PDF](stat566-all.pdf) | All four notes | 53 pages total |
| [Note 1](stat566-note01.pdf) | Potential outcomes, randomization, partial identification | `stat566-note01.pdf`, 9 pages |
| [Note 2](stat566-note02.pdf) | DAGs, LMP/GMP, factorization, d-separation, causal identification | `stat566-note02.pdf`, 22 pages |
| [Note 3](stat566-note3.pdf) | Regression, stratification, IPW, AIPW, ATT, DiD | `stat566-note3.pdf`, 12 pages |
| [Note 5](stat566-note5.pdf) | IV, 2SLS, diagnostics, LATE, Mendelian randomization | `stat566-note5.pdf`, 10 pages |

The original numbering is retained; there was no Note 4 among the supplied files. The typeset version reorganizes prose and expands formulas rather than reproducing the original page layout. Repeated calculations are consolidated. Graphs are represented by vector diagrams and/or explicit edge lists and path formulas.

Yellow boxes preserve TODOs and explain their status. Red boxes document corrections. Blue boxes mark lecture-based or explanatory supplements. Gray boxes clarify marginal questions. Source markers and [SOURCE-MAP.md](SOURCE-MAP.md) trace coverage back to the original pages. [LOG.log](LOG.log) records limitations and verification.

## Rebuild

Requires a reasonably complete TeX Live / MacTeX installation with LuaLaTeX, `newcomputermodern`, `tcolorbox`, and TikZ, plus Python 3 (standard library only):

```sh
python3 build.py
```

The script compiles each document at least twice (repeating if cross-references need another pass), checks for overfull boxes, missing glyphs, and undefined references, and copies final PDFs out of `build/`. The combined volume compiles from the same chapter files, so no content has to be maintained twice. Intermediate build files are excluded from version control.

The preamble follows `latex-template.tex` with the same page size, margins, 12-point text, and rounded breakable remark boxes. It uses New Computer Modern for consistent text and math rather than mixing two font families.

### Math delimiter convention

`TASK.md` specifically requests `$$...$$` for inline mathematics. Standard TeX interprets that as display math. To honor the requested source convention while keeping actual inline layout, `preamble.tex` defines the active paired `$$...$$` delimiter to call `\ensuremath`. Every displayed derivation uses `equation` or `align`; there are no `\[...\]` displays. Compile through the provided wrappers, which load this preamble; chapter files are not standalone documents.

## Editorial scope

All 53 source pages were visually inspected. Embedded PDF text was useful as a search aid but contains recognition errors; it was not copied uncritically. English translations preserve the mathematical meaning of Chinese annotations. Lecture passages are paraphrased and cited by lecture and section. No recordings were supplied, so TODOs that only specify times remain explicitly qualified. These are study notes, not an assertion that every unexplained handwritten abbreviation has been decoded.
