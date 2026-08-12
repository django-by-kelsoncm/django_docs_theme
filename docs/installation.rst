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

Testando Modificações Locais Antes do Commit
---------------------------------------------

Sempre que alterar arquivos CSS, JS ou templates do tema, siga este fluxo de teste local:

1. **Compilar a documentação oficial**:

   .. code-block:: bash

      sphinx-build -W -b html docs docs/_build/html

2. **Compilar a documentação dos exemplos**:

   .. code-block:: bash

      sphinx-build -W -b html docs/examples docs/examples/_build/html

3. **Subir o servidor HTTP local**:

   .. code-block:: bash

      cd docs/_build/html
      python3 -m http.server 8000

4. **Navegar e validar**:

   Abra o endereço ``http://localhost:8000`` no navegador para inspecionar os estilos, responsividade e Dark Mode.
