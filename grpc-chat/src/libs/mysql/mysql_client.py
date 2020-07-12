import pymysql
from pymysql import MySQLError
from src.libs.config.environment_config import EnvironmentConfig


class MySQLClient:

    def __init__(self):
        config = EnvironmentConfig()

        self.connection = pymysql.connect(
            host=config.mysql_host,
            user=config.mysql_user,
            password=config.mysql_password,
            port=config.mysql_port,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

        if config.mysql_database:
            self.connection.select_db(config.mysql_database)

    def execute_query(self, query: str, params, database=None, commit: bool = False):
        if database:
            self.connection.select_db(database)

        cursor = self.connection.cursor()

        try:
            cursor.execute(query, params)
            if commit:
                self.connection.commit()
        except MySQLError as e:
            self.rollback()
            raise e

        return cursor

    def rollback(self):
        self.connection.rollback()

        if self.connection.open:
            self.connection.close()

    def __del__(self):
        if self.connection.open:
            self.connection.close()
