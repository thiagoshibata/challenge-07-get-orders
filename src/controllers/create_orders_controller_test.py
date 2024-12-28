""" from src.models.repositories.orders_repository import OrdersRepository
from src.controllers.create_orders_controller import CreateOrdersController
from src.models.settings.db_connection_handler import db_connection_handler

def test_create_user_controller():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repo = OrdersRepository(conn)
    controller = CreateOrdersController(repo)

    user_id = 2
    description = "BOLO"

    response = controller.create(user_id, description)

    print()
    print(response) """