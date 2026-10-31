# STAT 581 Notes 3–4: Source Map

Updated October 30, 2026. All ten pages of the two newly supplied PDFs were visually inspected. Original files were found in `stat516-stochastic/notes/` and copied unchanged to `stat581-adv-stat-theory/notes/`. The original handwriting is retained locally, rather than included in this publication.

## Note 3

Retains the prior 31-page handwriting transcription and Lecture 2 supplements, including the seven illustrated distances. The new `stat581-note3 (2).pdf` is a continuation rather than a replacement of that 31-page source.

| New source page | Destination / treatment |
|---|---|
| 1 | Repeated unfinished ratio expansion from original p.31; TODO completed in “October 28 continuation: exact remainders and unequal rates” |
| 2 | Fixed population means, shrinking errors, ratio subtraction and reciprocal expansion; expanded with an exact identity |
| 3 | Linearized CLT, rate motivation, and TODO comparing direct expansion with the delta method; AIPW/IPW marginal note answered as an editorial supplement |
| 4 | Blank grid page, no substantive content |

Corrections: the ratio remainder contains both the product of numerator/denominator errors and the squared denominator error. Under root-n rates both are O_P(1/n). Unequal-rate statements require a joint limiting distribution and a negligible scaled remainder; no universal CLT is asserted. Coordinate ordering in the CLT and covariance is explicit. Both new TODOs are preserved in yellow boxes.

Reference: Yen-Chi Chen, *Lecture 2: Introduction of large sample theory*, Autumn 2026. No October 28 teacher handwriting was provided; the exact remainder and AIPW discussion are labeled editorial explanations.

## Note 4

| New source page | Destination / treatment |
|---|---|
| 1 | Likelihood, model misspecification, pseudo-true population maximizer; distinction between pointwise and uniform LLN |
| 2 | Score equations, parameter versus data gradients, handwritten M1; local assumption labels distinguished from lecture numbering |
| 3 | Fixed-target IID score CLT and Taylor identity; explicit explanation of data-dependent plug-in dependence |
| 4 | Interior target, Hessian LLN, absolute integrability, matrix inversion, and justified remainder control |
| 5 | Sandwich covariance, correct-model information identity, plug-in estimation and covariance scaling |
| 6 | Blank grid page, no substantive content |

No explicit TODO marker occurs in this source. Red boxes correct the Taylor remainder sign and the information identity: score second moment equals the negative expected log-likelihood Hessian under correct specification and regularity. Added supporting assumptions include consistency, finite score variance, and local uniform Hessian convergence. General covariance formulas use the inverse transpose; symmetry reduces it to an inverse.

Reference: Yen-Chi Chen, *Lecture 3: M-estimation and the maximum likelihood estimator*, Autumn 2026, especially Theorem 3.1. Existing later lecture complements (general M-estimation, influence functions, QMD/LAN, nuisance parameters, and optimization appendices) are retained and identified as extending beyond the five handwritten pages.

## Verification

Both standalone TeX sources were compiled repeatedly with XeLaTeX until contents/references stabilized, checked for missing glyphs and overflowing boxes, and visually reviewed using rendered PDF pages. The source PDFs are not required to rebuild the published notes.
