# 🐘 Neon CRUD Project

Este projeto é uma aplicação Python simples e modular para realizar operações CRUD (Create, Read, Update, Delete) utilizando PostgreSQL via [NeonDB](https://neon.tech).  
O código foi organizado em módulos para facilitar a leitura, manutenção e escalabilidade do sistema.

---

## 📁 Estrutura do Projeto

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
