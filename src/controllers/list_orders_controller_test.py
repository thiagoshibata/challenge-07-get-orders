""" from src.models.repositories.orders_repository import OrdersRepository
from src.controllers.list_orders_controller import ListOrdersController
from src.models.settings.db_connection_handler import db_connection_handler

def test_login_creator_controller():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repo = OrdersRepository(conn)
    controller = ListOrdersController(repo)

    # username = "user_test_controller"
    # password = "12345"


    response = controller.list_orders(2)

    print()
    print(response) """