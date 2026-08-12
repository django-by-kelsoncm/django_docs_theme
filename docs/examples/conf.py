# Configuration file for Sphinx documentation builder.
import os
import sys

# Add path to django_docs_theme if installed locally
sys.path.insert(0, os.path.abspath('../../'))

import django_docs_theme

project = 'Minha Suite Django'
copyright = '2026, Minha Organização'
author = 'Desenvolvedor'
release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

html_theme = 'django_docs_theme'
html_theme_path = [django_docs_theme.get_html_theme_path()]

html_theme_options = {
    'primary_color': '#0c4b33',
    'secondary_color': '#44b78b',
    'project_name': 'Minha Suite Django',
    'github_url': 'https://github.com/usuario/meu-projeto',
    'github_repo': 'usuario/meu-projeto',
    'github_version': 'main',
    'doc_path': 'docs/',
    'show_edit_on_github': True,
    'enable_dark_mode': True,
    'navigation_links': 'Início|index.html, Instalação|installation.html, Tutorial|tutorial.html, Referência|reference.html, GitHub|https://github.com/usuario/meu-projeto',
}

html_static_path = ['_static']
html_css_files = ['css/custom.css']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'django': ('https://docs.djangoproject.com/en/stable/', None),
}
