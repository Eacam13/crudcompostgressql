def salvar_registro(db_conn, nome, email):
    conn = db_conn.get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO registros (nome, email) VALUES (%s, %s)",
                (nome, email)
            )
            conn.commit()
            print("✅ Registro salvo com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao salvar registro: {e}")
        conn.rollback()
    finally:
        db_conn.release_conn(conn)
