============
Configuração
============

Saiba como configurar as opções do tema no arquivo ``conf.py`` da sua documentação.

Configuração Mínima
-------------------

No arquivo ``conf.py``:

.. code-block:: python

   import django_docs_theme

   html_theme = 'django_docs_theme'
   html_theme_path = [django_docs_theme.get_html_theme_path()]

Opções Disponíveis (``html_theme_options``)
--------------------------------------------

.. list-table::
   :widths: 25 20 55
   :header-rows: 1

   * - Opção
     - Padrão
     - Descrição
   * - ``primary_color``
     - ``#0c4b33``
     - Cor primária do cabeçalho, rodapé e títulos.
   * - ``secondary_color``
     - ``#44b78b``
     - Cor secundária para destaques e hover em links.
   * - ``project_name``
     - Nome do projeto
     - Nome exibido no cabeçalho ao lado do logotipo.
   * - ``logo``
     - ``""``
     - Caminho da imagem de logo dentro da pasta ``_static/``.
   * - ``logo_height``
     - ``36px``
     - Altura da imagem do logotipo no cabeçalho.
   * - ``github_url``
     - ``""``
     - URL completa do repositório no GitHub.
   * - ``github_repo``
     - ``""``
     - Repositório no formato ``owner/repo`` para o botão Edit on GitHub.
   * - ``github_version``
     - ``"main"``
     - Branch de referência no GitHub.
   * - ``show_edit_on_github``
     - ``True``
     - Habilita/desabilita o botão "Editar no GitHub".
   * - ``enable_dark_mode``
     - ``True``
     - Habilita/desabilita o botão de alternância do Dark Mode.
   * - ``navigation_links``
     - ``""``
     - String formatada como ``"Título|url, Título2|url2"``.
