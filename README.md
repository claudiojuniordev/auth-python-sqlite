<<<<<<< HEAD
### *Sistema de authenticação simples feita em Python*
*Ferramentas utilizadas*
- SQLite
- .venv (ambiente virtual)
- Biblioteca bcrypt
=======
# Sistema de Autenticação Python + SQLite

Este projeto implementa um sistema de autenticação básico usando Python e SQLite, com duas interfaces disponíveis:

## 1. Interface Web (Flask)
Interface gráfica moderna acessível via navegador.

### Como executar a versão web:
```bash
# Com o venv ativado:
python app.py
```
Depois acesse: http://localhost:5000

Recursos da versão web:
- Interface gráfica moderna
- Dashboard com informações do usuário
- Gerenciamento de usuários
- Feedback visual de ações
- Layout responsivo

## 2. Interface CLI (Terminal)
Versão em linha de comando para uso via terminal.

### Como executar a versão CLI:
```bash
# Com o venv ativado:
python cli/main.py
```

Recursos da versão CLI:
- Menu interativo no terminal
- Operações básicas de usuário
- Ideal para testes rápidos
- Não requer navegador

## Estrutura do Projeto
```
auth-python-sqlite/
├── app.py              # Aplicação Web (Flask)
├── cli/
│   └── main.py        # Interface de linha de comando
├── services/
│   └── auth_service.py # Lógica de autenticação
├── db/
│   ├── connection.py   # Conexão com SQLite
│   └── create_tables.py # Criação do banco
├── static/
│   └── css/           # Estilos da interface web
└── templates/         # Templates HTML
```

## Configuração
1. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate     # Linux/Mac
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Desenvolvimento
- `app.py`: Versão web com Flask
- `cli/main.py`: Versão terminal
- Ambas as versões compartilham o mesmo backend (`services/auth_service.py`)
- O banco de dados é compartilhado entre as duas interfaces
>>>>>>> 26057df (feat: Adiciona interface web com Flask e reorganiza projeto)
