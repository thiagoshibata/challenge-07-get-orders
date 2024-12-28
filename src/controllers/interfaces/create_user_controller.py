from abc import ABC, abstractmethod

class CreateUserControllerInterface(ABC):
    @abstractmethod
    def create(self, username: str, password: str, email: str) -> dict:
        pass