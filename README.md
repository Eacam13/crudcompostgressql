# 🐘 Neon CRUD Project

Este projeto é uma aplicação Python simples e modular para realizar operações CRUD (Create, Read, Update, Delete) utilizando PostgreSQL via [NeonDB](https://neon.tech).  
O código foi organizado em módulos para facilitar a leitura, manutenção e escalabilidade do sistema.

---

## 📁 Estrutura do Projeto

neon_crud_project/
│
├── .env # Variáveis de ambiente (URL do banco de dados)
├── main.py # Execução principal com menu interativo
│
├── db/
│ ├── connection.py # Gerenciamento de conexão com PostgreSQL
│ └── table_manager.py # Criação de tabelas
│
├── crud/
│ ├── create.py # Inserção de registros
│ ├── read.py # Leitura/listagem de registros
│ ├── update.py # Atualização de registros
│ └── delete.py # Remoção de registros (único ou todos)
│
└── utils/
└── menu.py # Menu interativo de terminal

yaml
Copiar
Editar

---

## ⚙️ Requisitos

- Python 3.9+
- PostgreSQL (NeonDB ou local)
- `pip` para instalar dependências

---

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/neon_crud_project.git
cd neon_crud_project
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Crie um arquivo .env com a URL do banco:

env
Copiar
Editar
DATABASE_URL=postgresql://usuario:senha@host:porta/nome_do_banco
▶️ Como usar
Execute o arquivo principal:

bash
Copiar
Editar
python main.py
Menu interativo:

css
Copiar
Editar
📌 MENU
1 - Adicionar novo registro
2 - Listar registros
3 - Deletar registro por ID
4 - Deletar todos os registros
5 - Atualizar registro por ID
6 - Sair
✅ Funcionalidades
Criar registros (nome, email)

Listar todos os registros ordenados por data

Atualizar um registro específico por ID

Deletar um único registro por ID

Deletar todos os registros da tabela

Estrutura de código limpa e separada em módulos

📚 Tecnologias utilizadas
Python

PostgreSQL

psycopg2

python-dotenv

Banco de dados Neon (alternativa serverless para PostgreSQL)

📌 Melhorias Futuras
Adicionar testes unitários com pytest

Interface Web ou REST API

Exportar registros em CSV/Excel

Autenticação de usuário

👨‍💻 Autor
Desenvolvido por Seu Nome com dedicação e foco em boas práticas.
Contribuições são bem-vindas!

📝 Licença
Este projeto está licenciado sob a Licença MIT.
