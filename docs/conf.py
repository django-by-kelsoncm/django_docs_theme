# Configuration file for Sphinx documentation of django-docs-theme
import os
import sys

# Ensure package root is in Python path
sys.path.insert(0, os.path.abspath('..'))

import django_docs_theme

project = 'django-docs-theme'
copyright = '2026, Django Tools Team'
author = 'Django Tools Team'
release = '0.1.1'

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
    'project_name': 'django-docs-theme',
    'github_url': 'https://github.com/django-by-kelsoncm/django_docs_theme',
    'github_repo': 'django-by-kelsoncm/django_docs_theme',
    'github_version': 'main',
    'doc_path': 'docs/',
    'show_edit_on_github': True,
    'enable_dark_mode': True,
    'navigation_links': 'Início|index.html, Instalação|installation.html, Configuração|configuration.html, Customização|customization.html, CI/CD & Workflows|workflow.html, GitHub|https://github.com/django-by-kelsoncm/django_docs_theme',
}

html_static_path = ['_static']
html_css_files = ['css/custom.css']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'django': ('https://docs.djangoproject.com/en/stable/', None),
}
