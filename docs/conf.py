# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'nomiden'
copyright = '2023, Diva K'
author = 'Diva K'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser'
]

# autoapi_dirs = ["../nomiden"]

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'