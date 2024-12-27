from sqlite3 import Connection
from src.models.interfaces.user_repository import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    
    def create_user(self, username: str, password: str, email: str) -> None:

        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO users 
                (username, password, email)
                VALUES (?, ?, ?)
            ''', (username, password, email)
        )
        self.__conn.commit()
    
    def get_user_by_username(self, username: str) -> tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM users WHERE username = ?
            ''', (username,)
        )
        user = cursor.fetchone()
        return user
