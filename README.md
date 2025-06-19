# CRUD Python com PostgreSQL (NeonDB)

Este projeto é uma aplicação de linha de comando para gerenciamento de registros (CRUD) utilizando Python e PostgreSQL hospedado na NeonDB. Ele permite adicionar, listar, atualizar e deletar registros de forma simples e eficiente.

---

## Funcionalidades

- Adicionar novo registro (nome e email)
- Listar todos os registros
- Atualizar registro por ID
- Deletar registro por ID
- Deletar todos os registros

---

## Pré-requisitos

- Python 3.10 ou superior
- [pip](https://pip.pypa.io/en/stable/)
- Conta e banco de dados criados na [NeonDB](https://neon.tech/)
- Variáveis de ambiente configuradas

---

## Instalação

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/Eacam13/crudcompostgressql.git
   cd pastadoprojeto
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```
   > Se não houver um arquivo `requirements.txt`, instale manualmente:
   ```sh
   pip install psycopg2-binary python-dotenv
   ```

---

## Configuração do Banco de Dados

1. **Crie um banco de dados PostgreSQL na [NeonDB](https://neon.tech/).**
2. **Obtenha a URL de conexão (exemplo):**
   ```
   postgresql://usuario:senha@endereco/neondb?sslmode=require
   ```
3. **Configure o arquivo [`.env.local`](.env.local ) na raiz do projeto:**

   ```
   DATABASE_URL=postgresql://usuario:senha@endereco/neondb?sslmode=require
   ```

   > **Nunca compartilhe sua URL de conexão publicamente.**

---

## Executando o Projeto

```sh
python main.py
```

O menu será exibido no terminal para interação.

---

## Estrutura do Projeto

```
.
├── main.py
├── crud/
│   ├── create.py
│   ├── read.py
│   ├── update.py
│   ├── delete.py
│   └── __init__.py
├── db/
│   ├── connection.py
│   ├── table_manager.py
│   └── __init__.py
├── ui/
│   └── menu.py
├── .env
├── .env.local
└── .gitignore
```

---

## Observações

- O projeto utiliza pool de conexões para melhor desempenho.
- As variáveis de ambiente são carregadas automaticamente pelo `python-dotenv`.
- O banco de dados é criado automaticamente na primeira execução, caso não exista.

---

## Licença

Este projeto está sob a licença MIT.

---

## Autor

Celio Almeida 
Linkedin: (https://www.linkedin.com/in/acamdeveloper/)

---

**Contribuições são bem-vindas!**
