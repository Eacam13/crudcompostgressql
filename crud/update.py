def atualizar_registro(db_conn, id, novo_nome, novo_email):
    conn = db_conn.get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE registros SET nome = %s, email = %s WHERE id = %s",
                (novo_nome, novo_email, id)
            )
            if cur.rowcount == 0:
                print("⚠️ Nenhum registro com esse ID.")
            else:
                conn.commit()
                print("✅ Registro atualizado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao atualizar registro: {e}")
        conn.rollback()
    finally:
        db_conn.release_conn(conn)
