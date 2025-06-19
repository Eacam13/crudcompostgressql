def deletar_registro_por_id(db_conn, id):
    conn = db_conn.get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM registros WHERE id = %s", (id,))
            if cur.rowcount == 0:
                print("⚠️ Nenhum registro encontrado com esse ID.")
            else:
                conn.commit()
                print("✅ Registro deletado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao deletar registro: {e}")
        conn.rollback()
    finally:
        db_conn.release_conn(conn)


def deletar_todos_registros(db_conn):
    conn = db_conn.get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM registros")
            conn.commit()
            print("✅ Todos os registros foram deletados.")
    except Exception as e:
        print(f"❌ Erro ao deletar todos os registros: {e}")
        conn.rollback()
    finally:
        db_conn.release_conn(conn)
