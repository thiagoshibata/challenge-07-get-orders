from src.models.interfaces.user_repository import UserRepositoryInterface
from src.controllers.interfaces.create_user_controller import CreateUserControllerInterface
from src.drivers.password_handler import PasswordHandler

class CreateUserController(CreateUserControllerInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository
        self.__password_handler = PasswordHandler()
    
    def create(self, username: str, password: str, email: str) -> dict:
        hashed_password = self.__create_hashed_password(password)
        self.__create_new_user(username, hashed_password, email)
        return self.__format_response(username, email)

    def __create_hashed_password(self, password: str) -> str:
        hashed_password =  self.__password_handler.encrypt_password(password)
        return hashed_password
    
    def __create_new_user(self, username: str, hashed_password: str, email: str) -> None:
        self.__user_repository.create_user(username, hashed_password, email)

    def __format_response(self, username: str, email: str) -> dict:
        return {
            "type": "User",
            "count": 1,
            "username": username,
            "email": email
        }

    
        