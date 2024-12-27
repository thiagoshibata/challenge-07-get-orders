from abc import ABC, abstractmethod

class OrdersRepositoryInterface(ABC):
    @abstractmethod
    def create_order(self, user_id: int, description: str) -> None:
        pass

    @abstractmethod
    def get_order_by_user_id(self, user_id: int) -> tuple:
        pass