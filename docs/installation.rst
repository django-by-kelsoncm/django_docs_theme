==========
Instalação
==========

Existem diversas maneiras de instalar o ``django-docs-theme`` no seu ambiente de desenvolvimento.

Via PyPI
--------

Instale a versão estável publicada no PyPI:

.. code-block:: bash

   pip install django-docs-theme

Instalação Direta do GitHub
----------------------------

Para instalar a versão de desenvolvimento diretamente do repositório no GitHub:

.. code-block:: bash

   pip install git+https://github.com/django-by-kelsoncm/django_docs_theme.git

Desenvolvimento Local
---------------------

Se você deseja modificar ou contribuir com o tema:

.. code-block:: bash

   git clone https://github.com/django-by-kelsoncm/django_docs_theme.git
   cd django_docs_theme
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e .
