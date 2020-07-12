from src.libs.mysql.mysql_client import  MySQLClient


class UserModel:

    def __init__(self):
        self.mysql_client = MySQLClient()

    def is_user_exits(self, username: str) -> bool:
        sql = "SELECT username, password FROM users WHERE username = %s"
        params = (username,)
        cursor = self.mysql_client.execute_query(query=sql, params=params)

        if cursor.rowcount > 0:
            return True
        else:
            return False
