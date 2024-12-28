from abc import ABC, abstractmethod

class LoginCreatorControllerInterface(ABC):
    @abstractmethod
    def create(self, username: str, password: str) -> dict:
        pass