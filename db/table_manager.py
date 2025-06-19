class TableManager:
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def create_registros_table(self):
        conn = self.db_conn.get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS registros (
                        id SERIAL PRIMARY KEY,
                        nome VARCHAR(100) NOT NULL,
                        email VARCHAR(100) NOT NULL,
                        data_criacao TIMESTAMP DEFAULT NOW()
                    )
                """)
                conn.commit()
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
        finally:
            self.db_conn.release_conn(conn)
