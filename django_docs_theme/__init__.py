"""
django_docs_theme - A reusable Sphinx HTML theme inspired by official Django documentation.
"""

import os
from typing import Dict, Any

__version__ = "0.1.0"


def get_html_theme_path() -> str:
    """
    Return the absolute path to the directory containing theme.conf.
    
    This function is maintained for backward compatibility with older Sphinx theme patterns.
    Modern Sphinx 1.6+ discovers the theme automatically via entry points.
    """
    return os.path.abspath(os.path.dirname(__file__))


def setup(app: Any) -> Dict[str, Any]:
    """
    Sphinx extension setup function.
    
    Registers the theme with Sphinx when activated in conf.py.
    """
    theme_path = get_html_theme_path()
    app.add_html_theme("django_docs_theme", theme_path)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
