================================
CI/CD, Workflows & Testes Locais
================================

Este projeto conta com automação completa via **GitHub Actions** para testes de CI, deploy automático no PyPI e publicação da documentação.

GitHub Workflows Configurados
-----------------------------

Os workflows estão salvos em ``.github/workflows/``:

1. **CI e Build da Documentação (``ci.yml``)**
   - Executa a cada `push` e `pull_request` nas branches `main` ou `master`.
   - Instala o Python, compila a documentação com Sphinx e valida a compilação de empacotamento PyPI.
   - Publica automaticamente a documentação atualizada no **GitHub Pages**.

2. **Deploy Automático no PyPI (``publish-pypi.yml``)**
   - Disparado automaticamente sempre que uma nova **Release** é publicada no GitHub.
   - Utiliza **PyPI Trusted Publishing** (OIDC federado do GitHub Actions sem necessidade de senhas ou tokens fixos expostos).
   - Constrói a distribuição de código (``sdist`` e ``wheel``) e realiza a publicação direta no PyPI.

Testando Workflows Locais com ``act``
-------------------------------------

O ``act`` é uma ferramenta de linha de comando que permite rodar seus workflows do GitHub Actions localmente através do Docker.

Pré-requisitos
~~~~~~~~~~~~~~

- Docker instalado e em execução.
- Ferramenta ``act`` instalada (ex: ``sudo apt install act`` ou ``brew install act``).

Comandos para Executar com ``act``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para rodar o evento de ``push`` simulado localmente:

.. code-block:: bash

   act push --container-architecture linux/amd64

Para rodar um job específico (ex: ``build``):

.. code-block:: bash

   act -j build --container-architecture linux/amd64

Para simular o disparo de publicação de release:

.. code-block:: bash

   act release -e .github/workflows/event_release.json --container-architecture linux/amd64
