========
Tutorial
========

Como aplicar o tema no arquivo ``conf.py``:

.. code-block:: python

   import django_docs_theme

   html_theme = 'django_docs_theme'
   html_theme_path = [django_docs_theme.get_html_theme_path()]
