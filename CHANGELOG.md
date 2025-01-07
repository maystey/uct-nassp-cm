# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
the version number, `a.b.c`, follows the following scheme:

- `a`. The edition (0 for the initial, incomplete edition), this will generally change on a yearly basis.
- `b`. New chapter(s) added or drastically changed.
- `c`. New sections, corrections, etc. The number change is consecutive, not reflecting the number of changes.


## [3.1.0] - 2022-01-07

### Added

- Seciton `scientific-packages/matplotlib/3d-plotting`

### Changed

- Updated to Jupyter-Book version ~~0.13.2~~ 0.15.1
- Updated requirements.txt to include pdfrw and pagelabels module
- Updated PDF book generation
- Corrections:
  - `numerical-methods/ode/higher-order`
    - Missing IVs for 2nd order differential equations
    - Some "n"s should have been "m" in the Higher Order ODE section
  - `numerical-methods/curve-fitting/linear-regression` x_j were referred to as "dependant variable", corrected to "independent variables"
  - `numerical-methods/integration/simpson` first summation term in composite method started from "i=2", corrected to "i=1"


## [3.0.1] - 2022-02-14

### Added

- Section `numerical-methods/curve-fitting/curve-fitting`

### Changed

- Update to Jupyter-Book version 0.11.2 .
- PDF export has been improved and the document is now ready for distribution.
- Rename Chapter `numerical-methods/regression` to `numerical-methods/curve-fitting`.
- Rewrote Sections:
 - `python-standard-library/functions/arguments`
 - `python-standard-library/functions/local-variables`

### Removed

- Outdated `environment.yml` file

## [2.2.0] - 2021-08-17

### Changed

- Rewrote chapter:
  - `numercial-methods/integration`
- Changed bibliography label prefix format.
- Corrected mistake in `references.bib`: Efferson -> Epperson


## [2.1.0] - 2021-08-13

### Added

- Added part `numerical-methods`
- Added page `standard-library/if-statements/nested`
- Add custom css for 
  - formatting tables: `table.css`
  - worked examples: `worked_example_div.css`

### Changed

- Updated to Jupyter-Book version 0.10.
- Added CC BY-SA 4.0 license button to first page.
- Moved `list-comprehension` page from `standard-library/loops` to `standard-library/data-structures/lists`.
- Re-wrote chapters:
  - `standard-library/if-statements`
  - `standard-library/loops`
  - `numerical-methods/ode`
  - `numerical-methods/regression`
- Change `_toc` chapter titles:
  - **Control Flow: If Statements** to **If Statements**
  - **Control Flow: Loops** to **Loops**

### Removed

- Removed Chapter: `numerical-methods/benchmarking`

## [2.0.2] - 2020-12-07

### Added

- Add scripts to generate pdf version of the book (WIP)

## [2.0.1] - 2020-12-01

### Added

- Added section Standard Library/If Statements/Inclusion Operators

### Changed

- Update to Jupyter-Book version 0.8

### Fixed

- Citations: labels are now unique and bibliography doesn't list uncited references.

## [2.0.0] - 2020-11-25

This edition of the book branches off from version [v1.0.0](https://github.com/maystey/uct_nassp_cm/releases/tag/v1.0.0), the notes used in 2020.

### Changed

- Edition updated to 2 (for the 2021 course).
- Update to Jupyter-Book version 0.7. A new repository has been created for this due to different requirements.
- Content re-organized into 3 main parts:
  - Python Standard Library
  - Scientific Packages
  - Numerical Methods
- Citations altered to new syntax.

### Bugs

- Bibliography displays all references in bibtex file, not only the ones used on the page.
- Links between pages don't work.
