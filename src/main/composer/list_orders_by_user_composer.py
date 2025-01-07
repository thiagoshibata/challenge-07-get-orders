from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.orders_repository import OrdersRepository
from src.controllers.list_orders_controller import ListOrdersController
from src.views.list_orders_by_user_view import ListOrderByUserView

def list_orders_by_user_composer():
    connection = db_connection_handler.get_connection()

    model = OrdersRepository(connection)
    controller = ListOrdersController(model)
    view = ListOrderByUserView(controller)

    return view

