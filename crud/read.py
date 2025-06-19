def listar_registros(db_conn):
    conn = db_conn.get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, nome, email, data_criacao 
                FROM registros 
                ORDER BY data_criacao DESC
            """)
            registros = cur.fetchall()

            if not registros:
                print("⚠️ Nenhum registro encontrado.")
                return

            print("\n📋 Registros encontrados:")
            for reg in registros:
                print(f"ID: {reg[0]}, Nome: {reg[1]}, Email: {reg[2]}, Data: {reg[3]}")
    except Exception as e:
        print(f"❌ Erro ao listar registros: {e}")
    finally:
        db_conn.release_conn(conn)
