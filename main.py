from db.connection import DatabaseConnection
from db.table_manager import TableManager
from crud import (
    salvar_registro,
    listar_registros,
    atualizar_registro,
    deletar_registro_por_id,
    deletar_todos_registros
)
from ui.menu import menu

def main():
    db = DatabaseConnection()
    tables = TableManager(db)
    tables.create_registros_table()

    try:
        while True:
            opcao = menu()
            if opcao == "1":
                nome = input("Nome: ")
                email = input("Email: ")
                salvar_registro(db, nome, email)
            elif opcao == "2":
                listar_registros(db)
            elif opcao == "3":
                id = input("ID do registro a deletar: ")
                deletar_registro_por_id(db, id)
            elif opcao == "4":
                confirmar = input("Tem certeza que deseja deletar TODOS os registros? (s/n): ")
                if confirmar.lower() == "s":
                    deletar_todos_registros(db)
            elif opcao == "5":
                id = input("ID do registro a atualizar: ")
                nome = input("Novo nome: ")
                email = input("Novo email: ")
                atualizar_registro(db, id, nome, email)
            elif opcao == "6":
                break
            else:
                print("Opção inválida.")
    finally:
        db.close_all()
        print("🔒 Conexões encerradas.")

if __name__ == "__main__":
    main()
