# GEMINI-App-Docs-Dev

Development repo for public-facing [GEMINI App Docs](https://gemini-breeding.github.io/)

## Tools

Documentation is created with MkDocs, a static site framework that uses markdown for formatting docs pages.

Specifically, the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) package is used to maintain a consistent theme with the MUI styling in the app itself.

## Installation

The recommended way to install packages needed to build and serve mkdocs is to create a virtual environment and install the mkdocs-material pip package (or you may use the `requirements.txt` file provided).

```
python -m venv mkdocs-env
source mkdocs-env/bin/activate
pip install mkdocs-material mkdocs-glightbox
```

Note that if you are in a conda environment, you may need to `conda deactivate` before activating the virtual env.

## How to use

The [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) site has extensive documentation, as one would expect. The site itself is created using MkDocs.

In general, features of the site are configured in the `mkdocs.yml` file, where a number of plugins or extensions can also be added. The addition of the plugins will change the allowable syntax in the docs files to provide support for features like icons, tabbed views, and more. The contents of the docs can be found in the `docs/` directory, where each markdown file represents a page in the docs.

## Previewing site contents

After installing the packages above, use `mkdocs serve` to serve the site on port 8000 to prieview changes in your web browser as you edit.
