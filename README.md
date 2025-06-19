🐘 Neon CRUD Project
Este projeto é uma aplicação Python simples e modular para realizar operações CRUD (Create, Read, Update, Delete) utilizando PostgreSQL via NeonDB.
O código foi organizado em módulos para facilitar a leitura, manutenção e escalabilidade do sistema.

📁 Estrutura do Projeto:

neon_crud_project/
├── .env → Variáveis de ambiente (URL do banco de dados)
├── main.py → Execução principal com menu interativo

├── db/
│ ├── connection.py → Gerenciamento de conexão com PostgreSQL
│ └── table_manager.py → Criação da tabela de registros

├── crud/
│ ├── create.py → Inserção de registros
│ ├── read.py → Leitura/listagem de registros
│ ├── update.py → Atualização de registros
│ └── delete.py → Remoção de registros (único ou todos)

└── utils/
└── menu.py → Menu interativo de terminal

⚙️ Requisitos:

Python 3.9 ou superior

PostgreSQL (NeonDB ou local)

pip (gerenciador de pacotes Python)

📦 Instalação:

Clone o repositório:
git clone https://github.com/seu-usuario/neon_crud_project.git
cd neon_crud_project

Crie um ambiente virtual (opcional, mas recomendado):

Linux/macOS:
python -m venv venv
source venv/bin/activate

Windows:
python -m venv venv
venv\Scripts\activate

Instale as dependências:
pip install -r requirements.txt

Crie o arquivo .env com sua URL do banco:
DATABASE_URL=postgresql://usuario:senha@host:porta/nome_do_banco

▶️ Como usar:

Execute o arquivo principal:
python main.py

Você verá o menu interativo:

📌 MENU
1 - Adicionar novo registro
2 - Listar registros
3 - Deletar registro por ID
4 - Deletar todos os registros
5 - Atualizar registro por ID
6 - Sair

✅ Funcionalidades:

Criar registros (nome, email)

Listar todos os registros ordenados por data

Atualizar um registro específico por ID

Deletar um único registro por ID

Deletar todos os registros da tabela

Estrutura limpa e modular

📚 Tecnologias utilizadas:

Python

PostgreSQL

psycopg2

python-dotenv

NeonDB (PostgreSQL serverless)

📌 Melhorias Futuras:

Adicionar testes com pytest

Interface Web ou API REST

Exportar dados em CSV/Excel

Autenticação de usuários

👨‍💻 Autor:

Desenvolvido por Seu Nome com dedicação e foco em boas práticas.
Contribuições são bem-vindas!

📝 Licença:

Este projeto está licenciado sob a Licença MIT.
Verifique o arquivo LICENSE para mais detalhes.
