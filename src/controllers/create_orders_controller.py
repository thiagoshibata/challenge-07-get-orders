from src.models.interfaces.orders_repository import OrdersRepositoryInterface

class CreateOrdersController():
    def __init__(self, orders_repository: OrdersRepositoryInterface):
        self.__orders_repository = orders_repository
    
    def create(self, user_id: int, description: str) -> dict:
        response = self.__create_new_order(user_id, description)
        print()
        print(response)
        return self.__format_response(user_id, description)
    
    def __create_new_order(self, user_id: int, description: str) -> None:
        self.__orders_repository.create_order(user_id, description)

    def __format_response(self, user_id: int, description: str) -> dict:
        return {
            "type": "Order",
            "count": 1,
            "user_id": user_id,
            "description": description
        }

    
        