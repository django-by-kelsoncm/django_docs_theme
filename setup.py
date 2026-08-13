#!/usr/bin/env python
from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="django-docs-theme",
    version="0.1.8",
    author="Django Tools Team",
    author_email="kelson@example.com",
    description="Um tema Sphinx reutilizável e elegante para documentação de projetos Django",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/django-by-kelsoncm/django_docs_theme",
    packages=find_namespace_packages(include=["django_docs_theme*"]),
    include_package_data=True,
    package_data={
        "django_docs_theme": [
            "*.html",
            "theme.conf",
            "theme.toml",
            "static/css/*.css",
            "static/js/*.js",
            "templates/*.html",
            "templates/*/*.html",
        ],
    },
    entry_points={
        "sphinx.html_themes": [
            "django_docs_theme = django_docs_theme",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Documentation",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Software Development :: Documentation",
    ],
    python_requires=">=3.8",
)
