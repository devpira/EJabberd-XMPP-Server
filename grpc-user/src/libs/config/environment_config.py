import os


class EnvironmentConfig:

    mysql_host = None
    mysql_user = None
    mysql_password = None
    mysql_port = None
    mysql_database = None

    def __init__(self):
        self.mysql_host = os.environ.get("MYSQL_HOST").strip()
        self.mysql_user = os.environ.get("MYSQL_USER").strip()
        self.mysql_password = os.environ.get("MYSQL_PASSWORD").strip()
        self.mysql_port = os.environ.get("MYSQL_PORT")
        if not isinstance(self.mysql_port, int):
            self.mysql_port = int(self.mysql_port)
        self.mysql_database = os.environ.get("MYSQL_DATABASE").strip()
