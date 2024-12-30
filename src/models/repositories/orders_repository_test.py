""" from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.orders_repository import OrdersRepository

# teste de integração
def test_user_repository():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repo = OrdersRepository(conn)

    # user_id = 1
    # description = "order test"

    orders = repo.get_order_by_user_id(2)

    # order = repo.create_order(user_id, description)

    print()
    print(orders) """