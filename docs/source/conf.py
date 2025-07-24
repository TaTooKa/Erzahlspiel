# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Erzählspiel'
copyright = '2024, TaTooKa'
author = 'TaTooKa'

release = '0.1'
version = '0.2.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'hoverxref.extension',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
# html_theme = 'conestack'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for hoverxref
hoverxref_roles = [
    'numref',
    'confval',
    'setting',
    'footnote',
]
hoverxref_auto_ref = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = "_static/images/Erzahlspiel-logo.png"
html_theme_options = {
    'logo_only': True,
    'display_version': True,
}

def setup(app):
    app.add_css_file('css/custom.css')
