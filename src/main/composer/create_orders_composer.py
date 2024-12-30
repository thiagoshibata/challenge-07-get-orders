from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.orders_repository import OrdersRepository
from src.controllers.create_orders_controller import CreateOrdersController
from src.views.create_orders_view import CreateOrdersView

def create_orders_composer():
    connection = db_connection_handler.get_connection()
    model = OrdersRepository(connection)
    controller = CreateOrdersController(model)
    view = CreateOrdersView(controller)

    return view