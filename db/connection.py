import os
from psycopg2 import pool
from dotenv import load_dotenv

load_dotenv()

class DatabaseConnection:
    def __init__(self):
        self.pool = pool.SimpleConnectionPool(
            1,
            10,
            os.getenv('DATABASE_URL')
        )

    def get_conn(self):
        return self.pool.getconn()

    def release_conn(self, conn):
        self.pool.putconn(conn)

    def close_all(self):
        self.pool.closeall()
