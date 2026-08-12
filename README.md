# django-docs-theme

Um **tema Sphinx reutilizável** e altamente customizável criado para desenvolvedores Django e suites de projetos no GitHub. Inspirado no design limpo e profissional da [documentação oficial do Django](https://docs.djangoproject.com/), este tema permite manter uma identidade visual padronizada e moderna em todas as documentações da sua organização.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Sphinx](https://img.shields.io/badge/sphinx-4.0%2B-green)
![CI & Docs](https://github.com/django-by-kelsoncm/django_docs_theme/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue)

---

## 🚀 Recursos Principais

- 🎨 **Design Inspirado no Django**: Visual elegante com o característico verde escuro (`#0c4b33`), suporte a badges, tabelas responsivas e callouts (notes, warnings, tips).
- 🌙 **Modo Escuro (Dark Mode)**: Suporte a alternância de tema claro/escuro com detecção de preferência do sistema e salvamento no `localStorage`.
- ⚙️ **Customização Simples**: Altere cores primárias/secundárias, logotipo, fontes e links de navegação diretamente via `conf.py`.
- 📋 **Blocos de Código Interativos**: Botão para copiar snippets de código com um clique em todos os exemplos Python, HTML, Bash e SQL.
- ✏️ **Edit on GitHub**: Link automático para editar a página no repositório GitHub correspondente.
- 📱 **100% Responsivo**: Menu hamburguer e layout otimizado para dispositivos móveis e desktops.
- 📦 **Automação PyPI & GitHub Actions**: Deploy automático no PyPI a cada nova release via *Trusted Publishing*, compilação e deploy de docs no GitHub Pages e testes locais com `act`.

---

## 🛠️ Instalação

### Via PyPI

```bash
pip install django-docs-theme
```

### Instalação direta do GitHub

```bash
pip install git+https://github.com/django-by-kelsoncm/django_docs_theme.git
```

### Desenvolvimento Local

```bash
git clone https://github.com/django-by-kelsoncm/django_docs_theme.git
cd django_docs_theme
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

---

## ⚙️ Configuração Básica no `conf.py`

No arquivo `conf.py` da documentação do seu projeto Django, adicione:

```python
import django_docs_theme

# Registrar o tema
html_theme = 'django_docs_theme'
html_theme_path = [django_docs_theme.get_html_theme_path()]

# Opções do Tema
html_theme_options = {
    'primary_color': '#0c4b33',        # Verde primário do projeto
    'secondary_color': '#44b78b',      # Verde secundário para hover/destaques
    'project_name': 'Minha Suite Django',
    'logo': 'logo.png',                # Caminho relativo em _static/
    'logo_height': '36px',
    'github_url': 'https://github.com/usuario/meu-projeto',
    'github_repo': 'usuario/meu-projeto',
    'github_version': 'main',
    'doc_path': 'docs/',
    'show_edit_on_github': True,
    'enable_dark_mode': True,
    'navigation_links': 'Início|index.html, Instalação|installation.html, Tutorial|tutorial.html, Referência|reference.html',
}

# Arquivos estáticos customizados do projeto
html_static_path = ['_static']
html_css_files = ['css/custom.css']
```

---

## 🎨 Opções de Customização (`html_theme_options`)

| Opção | Padrão | Descrição |
| :--- | :--- | :--- |
| `primary_color` | `#0c4b33` | Cor primária usada no cabeçalho, rodapé e títulos principais. |
| `secondary_color` | `#44b78b` | Cor secundária usada em bordas, destaques e hover de links. |
| `project_name` | `project` | Nome do projeto exibido no cabeçalho ao lado da logo. |
| `logo` | `""` | Nome do arquivo de logo dentro do diretório `_static/`. |
| `logo_height` | `36px` | Altura do logotipo no cabeçalho. |
| `github_url` | `""` | URL completa do repositório no GitHub. |
| `github_repo` | `""` | Repositório no formato `owner/repo` para o link "Edit on GitHub". |
| `github_version` | `"main"` | Branch padrão do GitHub para o link de edição. |
| `doc_path` | `"docs/"` | Caminho do diretório de documentos no repositório. |
| `show_edit_on_github` | `True` | Exibe o botão "Editar no GitHub" na barra superior. |
| `enable_dark_mode` | `True` | Habilita o botão para alternar para o Modo Escuro. |
| `navigation_links` | `""` | String com links no formato `"Título\|url, Título2\|url2"`. |

---

## 💅 Sobrescrevendo Estilos (`_static/css/custom.css`)

Cada projeto pode sobrescrever variáveis CSS globais criando um arquivo `_static/css/custom.css`:

```css
:root {
  --django-primary: #005588;       /* Altera a cor principal para azul */
  --django-secondary: #0088cc;
  --font-sans: 'Inter', sans-serif;
}
```

---

## 📁 Estrutura do Repositório

```
django_docs_theme/
├── .github/
│   └── workflows/
│       ├── ci.yml             # Integracão contínua e deploy no GitHub Pages
│       ├── publish-pypi.yml   # Deploy automático no PyPI via Trusted Publishing
│       └── event_release.json # Payload simulado para testes locais com act
├── docs/                      # Documentação oficial do tema
│   ├── conf.py                # Configuração Sphinx usando django_docs_theme
│   ├── index.rst
│   ├── installation.rst
│   ├── configuration.rst
│   ├── customization.rst
│   ├── workflow.rst
│   └── examples/              # Exemplos completos para reutilização em novos projetos
│       ├── conf.py
│       ├── index.rst
│       ├── installation.rst
│       ├── tutorial.rst
│       └── reference.rst
├── django_docs_theme/         # Código fonte do tema Sphinx
│   ├── static/
│   │   ├── css/
│   │   │   ├── base.css
│   │   │   └── colors.css
│   │   └── js/
│   │       └── theme.js
│   ├── templates/
│   │   ├── layout.html
│   │   ├── page.html
│   │   ├── searchbox.html
│   │   └── breadcrumbs.html
│   ├── theme.conf
│   ├── theme.toml
│   └── __init__.py
├── setup.py                   # Empacotamento PyPI
├── pyproject.toml             # Metadados modernos do pacote Python
├── MANIFEST.in                # Inclusão de estáticos na distribuição
├── LICENSE
└── README.md
```

---

## 📖 Compilando a Documentação Localmente

Para compilar a documentação completa do projeto em `docs/`:

```bash
# 1. Ative o ambiente virtual e instale o pacote local
pip install -e .

# 2. Compile a documentação principal em HTML
sphinx-build -b html docs docs/_build/html

# 3. Ou compilar os exemplos contidos em docs/examples/
sphinx-build -b html docs/examples docs/examples/_build/html
```

---

## 🤖 GitHub Workflows & Deploy no PyPI

Este repositório está configurado com automação completa via GitHub Actions:

### 1. CI e GitHub Pages (`.github/workflows/ci.yml`)
- Disparado a cada `push` ou `pull_request` nas branches `main` e `master`.
- Testa a compilação estrita da documentação (`sphinx-build -W`).
- Gera o empacotamento PyPI (`python -m build`).
- Faz o deploy automático da documentação no **GitHub Pages**.

### 2. Publicação Automática no PyPI (`.github/workflows/publish-pypi.yml`)
- Disparado automaticamente sempre que uma nova **Release** é publicada no GitHub (`on: release`).
- Utiliza **PyPI Trusted Publishing** (autenticação OIDC segura sem armazenar tokens fixos).
- Compila e envia o pacote `sdist` e `wheel` para o PyPI.

### 3. Testando Workflows Locais com `act`

Você pode testar a execução dos workflows do GitHub Actions na sua máquina local utilizando a ferramenta [act](https://github.com/nektos/act) junto com o Docker:

```bash
# Listar todos os jobs reconhecidos pelo act
act -l

# Executar a pipeline de CI localmente
act push --container-architecture linux/amd64

# Executar apenas o job de Build & Validação
act -j build --container-architecture linux/amd64 -P ubuntu-latest=catthehacker/ubuntu:act-latest

# Simular o evento de publicação de release para o PyPI
act release -e .github/workflows/event_release.json --container-architecture linux/amd64
```

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.