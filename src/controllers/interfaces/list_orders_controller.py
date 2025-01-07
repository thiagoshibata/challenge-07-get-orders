from abc import ABC, abstractmethod

class ListOrdersControllerInterface(ABC):

    @abstractmethod
    def list_orders(self, user_id: int) -> dict:
        pass