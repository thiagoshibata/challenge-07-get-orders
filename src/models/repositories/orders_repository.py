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
                SELECT O.id, O.description, O.created_at, O.user_id , U.username  
                FROM orders as O
                INNER JOIN users as U 
                on O.user_id = U.id
                WHERE O.user_id = ?
            ''', (user_id,)
        )
        orders_user = cursor.fetchall()
        return orders_user
