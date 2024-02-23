# GEMINI-App-Docs-Dev
Development repo for public-facing GEMINI App Docs

## Tools

Documentation is created with MkDocs, a static site framework that uses markdown for formatting docs pages.

Specifically, the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) package is used to maintain a consistent theme with the MUI styling in the app itself.

## Installation

Packages needed to build and serve MkDocs can either be loaded from the python venv with `source mkdocs-env/bin/activate` or you can install the mkdocs-material pip package with `pip install mkdocs-material`.

## How to use

The [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) site has extensive documentation, as one would expect. The site itself is created using MkDocs.

In general, features of the site are configured in the `mkdocs.yml` file, where a number of plugins or extensions can also be added. The addition of the plugins will change the allowable syntax in the docs files to provide support for features like icons, tabbed views, and more. The contents of the docs can be found in the `docs/` directory, where each markdown file represents a page in the docs.
