from src.models.interfaces.orders_repository import OrdersRepositoryInterface

class ListOrdersController:
    def __init__(self, repository: OrdersRepositoryInterface) -> None:
        self.__repository = repository
    
    def list_orders(self, user_id: int) -> dict:
        orders = self.__repository.get_order_by_user_id(user_id)
        response_formated = self.__format_response(orders)

        return response_formated
    
    def __format_response(self, orders: list) -> dict:
        result = []
        for order in orders:
            result.append({
                "id": order[0],
                "description": order[1],
                "dt_order": order[2],
                "user_id": order[3],
                "username": order[4]
            })
        return result