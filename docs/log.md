# Log

How was this package built.

## 20250524

!!! success "Setup"
    - Setup a devcontainer.

!!! info "Tooling"
    - Started to utilise [uv](https://docs.astral.sh/uv/getting-started/) for python project  management.
    - Started to utilise [git-cliff](https://git-cliff.org/) for changelog generation.

!!! question "Docs"
    - Installed mkdocs and created [documentation in github pages](https://www.mkdocs.org/user-guide/deploying-your-docs/).
    - Leverage mkdocs [admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#supported-types).
    - Added [mkdocs-material](https://squidfunk.github.io/mkdocs-material/) theme.

### Useful Commands

```bash
python --version
uv --version
mkdocs gh-deploy
mkdocs serve
git-cliff -c cliff.toml
```

