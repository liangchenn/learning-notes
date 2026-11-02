# STAT 581 Notes 3–4: Source Map

Historical October 30, 2026 update. All ten pages of the two newly supplied PDFs were visually inspected. Original files were found in `stat516-stochastic/notes/` and copied unchanged to `stat581-adv-stat-theory/notes/`. The original handwriting is retained locally, rather than included in this publication.

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

## Note 4: historical October 30 source

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

## November 2 update: expanded Notes 4

The updated local `notes/stat581-note4.pdf` has 16 pages: pp. 1–15 contain handwriting and p. 16 is blank. Pages 6–15 replace the previous blank p. 6 and add the continuation supplied November 2 (p. 6 is dated November 1). The original pp. 1–5 remain covered.

- pp. 6–7: sandwich recap, computational motivation, empirical bootstrap algorithm, covariance scaling, confidence intervals and testing. The p. 7 TODO is answered with the distinction between nonconvexity, local regularity, boundary limits and numerical failure; neither bootstrap nor sandwich is automatically valid in nonregular settings.
- pp. 8–9: exact third-derivative remainder, absolute integrable envelope, coordinatewise intermediate points, integrated Hessian, interior versus compactness. The p. 9 TODO is answered: second derivatives can suffice with local uniform Hessian control; a common multivariate intermediate point need not exist.
- p. 10: the TODO on replacing M3 with compactness/M4 is answered using an anchor bound and a proper conditional-normal likelihood counterexample. Neither Hessian integrability nor nonsingularity follows from M4 alone.
- pp. 11–13: loss/risk/ERM, squared prediction loss, intercept, polynomial/orthonormal bases, learned features, neural regression and logistic classification. The feature-engineering question is answered; nonlinear covariate features can still be linear in coefficients, and learned features require accounting for their estimation.
- pp. 14–15: KDE bias/variance, density derivative versus log-density score, mode expansion and derivative variance. The p. 15 TODO is answered with sufficient bandwidth rates, a power-bandwidth range, the limiting variance, and the distinction between true-mode and smoothed-mode centering.
- p. 16: blank; no transcription required.

All four new TODOs are retained and answered in yellow boxes. Red boxes correct bootstrap covariance scaling and the density-derivative/score confusion; earlier information-identity and Taylor-sign corrections remain. Earlier Lecture 3 supplements are retained. All mathematical content uses equation/align environments and English prose. The self-contained Notes 4 PDF has 20 pages, compiled twice with XeLaTeX with no warnings, missing glyphs, undefined references, or overfull/underfull boxes. Rendered pages were visually checked.
