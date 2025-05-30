# Developer Diary

This document serves as a diary for the development of this package. It is intended to provide insights into the development process, decisions made, and tools used.

## 20250524

!!! success "Setup"
    - Setup a devcontainer.
    - Followed this blog for [uv setup a package](https://sarahglasmacher.com/how-to-build-python-package-uv/).

!!! info "Tooling"
    - Started to utilise [uv](https://docs.astral.sh/uv/getting-started/) for python project  management.
    - Started to utilise [git-cliff](https://git-cliff.org/) for changelog generation.

!!! question "Docs"
    - Installed mkdocs and created [documentation in github pages](https://www.mkdocs.org/user-guide/deploying-your-docs/).
    - Leverage mkdocs [admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#supported-types).
    - Added [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) theme.

## 20250225

!!! info "Tooling"
    - Add repo [copilot prompt](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot) to ensure uses conventional commits.
    - Investigated [coverage](https://coverage.readthedocs.io/en/7.2.7/) and [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) for code coverage. Unsure which one to use.
