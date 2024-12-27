from sqlite3 import Connection
from src.models.settings.db_connection_handler import db_connection_handler

class OrdersRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create_order(self, user_id: int, description: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO orders 
                (user_id, description)
                VALUES (?, ?)
            ''', (user_id, description)
        )
        self.__conn.commit()
    
    def get_order_by_user_id(self, user_id: int) -> tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM orders WHERE user_id = ?
            ''', (user_id,)
        )
        order = cursor.fetchone()
        return order
