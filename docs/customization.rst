============
Customização
============

Além das variáveis do `html_theme_options`, você pode customizar completamente os estilos visuais.

Customização via CSS
--------------------

Crie um arquivo ``_static/css/custom.css`` no seu projeto e referencie no ``conf.py``:

.. code-block:: python

   html_css_files = ['css/custom.css']

No arquivo ``custom.css``, você pode sobrescrever qualquer variável do tema:

.. code-block:: css

   :root {
     --django-primary: #1a5276;
     --django-secondary: #2980b9;
     --font-sans: "Inter", sans-serif;
   }

Variáveis CSS Disponíveis
--------------------------

- ``--django-primary``: Verde escuro padrão (`#0c4b33`)
- ``--django-secondary``: Verde claro padrão (`#44b78b`)
- ``--django-accent``: Fundo neutro de destaque (`#f1f1f1`)
- ``--django-text``: Cor do texto principal (`#2b2b2b`)
- ``--django-bg``: Fundo da página (`#ffffff`)
- ``--django-code-bg``: Fundo de blocos de código (`#f8f9fa`)
- ``--django-sidebar-bg``: Fundo do menu lateral (`#f8f9fa`)
