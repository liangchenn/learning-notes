# Source and editorial coverage map

Page numbers below refer to the handwritten PDFs in the original `notes/` directory. The output is a reorganized transcription with corrections and labeled supplements, not a facsimile. Every page, including blank pages and headings, is accounted for.

## Note 1 — `stat566-note01.pdf` (9 pages)

| Pages | Output section / treatment |
|---|---|
| 1–2 | Potential outcomes; ATE/ATT/ATC; binary response types; harmed-proportion question; randomized equality of population targets; SUTVA |
| 3 | Treatment variation irrelevance, consistency, no interference; vaccination example; reread-reference TODO resolved conceptually; `EQC?` preserved as undecoded shorthand |
| 4 | Identification under RCT; Neyman estimator and variance; corrected finite-population definitions and centered pivot |
| 5 | Fisher sharp null; reread TODO and “fill to 10:08” TODO preserved; randomization-test procedure supplied from Lecture 1 |
| 6 | Partial identification versus point identification; ACE/ATE terminology |
| 7 | Missing counterfactual decomposition; bounded-support Manski interval; zero endpoint and width questions answered |
| 8 | MTR definition; no-harm question; “complete” TODO supplied with sharp bounds and attainment argument |
| 9 | MTS definition; naive contrast as upper bound; corrected distinction between MTS and MTR+MTS |

Lecture sources: `Lecture1_Introduction_RandomizedExperiments (1).pdf`; `Lecture2_ManskiBounds_PartialIdentification (1).pdf`, Sections 1–3.

## Note 2 — `stat566-note02.pdf` (22 pages)

| Pages | Output section / treatment |
|---|---|
| 1–2 | Graphs, DAGs, Bayesian networks; path examples; kinship definitions; roots/sinks; self-inclusive ancestor/descendant convention |
| 3–4 | Parent factorization; local Markov; corrected missing Z in independence claim; graph enlargement; SCM equations |
| 5–6 | Three motifs with corrected fork/collider labels; Berkson's paradox; full blocking rule including descendants |
| 7–8 | Markov versus faithfulness; causal discovery context; LMP/GMP/factorization theorem and proof outline; equivalence classes |
| 9 | Recursive SCM generation, topological order, nonlinear functions, threshold treatment, random assignment |
| 10 | Incoming-edge removal; pooled t-test with corrected standard error; power/noncentrality |
| 11 | Mediator/collider adjustment in RCT; baseline precision qualifications |
| 12–13 | Intervention setup; truncated factorization; adjustment integral and mean; distinction from conditioning |
| 14–15 | Back-door criterion, parent adjustment, sufficient versus complete criteria, total effect versus regression coefficient qualifications, reverse-causation/no-directed-path implication |
| 16 | Larger graph transcribed as full edge list; both candidate paths; valid and minimal sets; collider Q example |
| 17 | Minimal back-door definition and distinction from minimum size/variance |
| 18 | Causal versus observational equivalence; intervention kernels; corrected faithfulness/uniqueness claims |
| 19 | Back-door recap; choosing covariates; all-baseline question and latent-variable M-bias exception |
| 20 | I/B/C/A/M/D/Y graph, candidate adjustment sets, variance roles; coefficient example |
| 21 | “Add SCM notes” TODO explicitly preserved and completed with intervention construction and consistency |
| 22 | Wright total-effect path rule; separate general covariance formula |

Lecture sources: `Lecture3_GraphicalModels_DAGs (2).pdf`, Sections 2–4; `Lecture3b_RCTs_and_DAGs (1).pdf`; `Lecture4_CausalDAGs_Identification.pdf`, Sections 1–4.

Editorial expansion: LMP→factorization via a topological chain rule; factorization→GMP via ancestral moralization; support/positivity qualifications; explicit unfaithful cancellation example; error-expansion covariance formula. These clarify the handwritten concepts and prevent treating accidental independence as a graphical guarantee.

## Note 3 — `stat566-note3.pdf` (12 pages)

| Pages | Output section / treatment |
|---|---|
| 1–2 | ATE target, identification assumptions, overlap, estimator list, general/additive/linear SCM distinctions |
| 3 | Birth-weight example and “fill to 9:02” TODO; outcome regression and standardization; model-dependence qualifications |
| 4 | Stratification estimator and population weights |
| 5 | Propensity score/balancing; HT estimator; “core idea” TODO completed |
| 6 | IPW iterated-expectation proof TODO completed; continuous-outcome correction; Hájek formula and intuition TODO; finite-sample and efficiency qualifications |
| 7 | Propensity fitting response corrected to A; score diagnostics, Love plot; SMD-definition TODO completed with stated denominator convention |
| 8 | Overlap; trimming versus clipping; symmetric clipping correction |
| 9 | ATT identification, target covariate distribution, corrected treated-sample denominator |
| 10 | Heterogeneity and CATE; corrected conditions for equality of ATE/ATT/CATE |
| 11 | “DiD Estimator” heading only; core two-period identification supplied as a labeled Lecture 6 supplement |
| 12 | Blank continuation page; no recoverable content omitted |

Lecture sources: `Lecture5_Estimation_StratIPW.pdf`, Sections 1–6; `Lecture6_ATT_DiD.pdf`. Matching and AIPW are supplied because the manuscript lists them; their added exposition is identified in the text.

## Note 5 — `stat566-note5.pdf` (10 pages)

| Pages | Output section / treatment |
|---|---|
| 1 | IV graph and assumptions; incoming-versus-outgoing graph operation; exclusion/exogeneity distinction |
| 2 | Linear SCM, covariance proof, Wald, indirect LS and 2SLS; stage naming and SE qualifications |
| 3 | Conditional IV; same controls in both stages; post-instrument control question; different-complier warning addressed by LATE section |
| 4 | Card schooling/wage graph, family and demographic concerns |
| 5 | OLS/IV comparison; first-stage F heuristic qualified; exclusion and exogeneity concerns |
| 6 | CHR direct-effect sensitivity; point-zero versus CI-zero threshold; Anderson–Rubin; “DID for IV — Ting Ye” retained as an unexpanded reading prompt |
| 7 | Partially linear IV residualization; missing final ratio supplied; cross-fitting qualification |
| 8 | “Multiple IV” heading only; 2SLS matrix form and overidentification discussion supplied as lecture supplement |
| 9 | “Binary IV” heading only; compliance types, monotonicity, LATE derivation supplied as lecture supplement |
| 10 | Mendelian randomization graph and two-sample idea; assumptions and harmonization clarified |

Lecture source: `Lecture8_InstrumentalVariables.pdf`, Sections 1–7 and 9. No external empirical data were downloaded, and no lecture example estimates are presented as newly computed results.
