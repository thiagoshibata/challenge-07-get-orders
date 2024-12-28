from abc import ABC, abstractmethod

class CreateOrdersControllerInterface(ABC):
    @abstractmethod
    def create(self, user_id: int, description: str) -> dict:
        pass