# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
the version number, `a.b.c`, follows the following scheme:

- `a`. The edition (0 for the initial, incomplete edition), this will generally change on a yearly basis.
- `b`. New chapter(s) added or drastically changed, the number increase is the number of chapters added/changed
- `c`. New sections, corrections, etc. The number change is consecutive, not reflecting the number of changes.

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
