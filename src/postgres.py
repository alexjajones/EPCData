import psycopg2

from config_utils import Config
from sqlalchemy import create_engine


class Postgres:
    conn = None

    def __init__(self, config):
        self.conn = self.get_connection(config)

    @staticmethod
    def get_connection(config: Config):
        return create_engine('postgres://{user}:{password}@{host}:5432/{database}'.format(
            host=config.postgres_host,
            user=config.postgres_user,
            password=config.postgres_password,
            database=config.postgres_db,
        ))

    def write_data(self, df, table_name):
        df.to_sql(table_name, self.conn, if_exists="replace")

    def read_data(self):
        return self.conn.execute("SELECT * FROM epc").fetchall()
