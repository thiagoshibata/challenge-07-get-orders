from src.models.interfaces.user_repository import UserRepositoryInterface
from src.controllers.interfaces.login_creator_controller import LoginCreatorControllerInterface
from src.drivers.password_handler import PasswordHandler
from src.drivers.jwt_handler import JwtHandler

class LoginCreatorController(LoginCreatorControllerInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
        self.__jwt_handler = JwtHandler()
        self.__password_handler = PasswordHandler()

    def create(self, username: str, password: str) -> dict:
        user = self.__find_user(username)
        user_id = int(user[0])
        hashed_password = user[2]

        self.__verify_password_correct(password, hashed_password)
        token = self.__create_jwt_token(user_id)
        return self.__format_response(username, user_id, token)


    def __find_user(self, username:str) -> dict:
        user = self.__user_repository.get_user_by_username(username)
        if not user: raise Exception('User not found')
        return user
    
    def __verify_password_correct(self, password: str, hashed_password: str) -> None:
        is_correct_password = self.__password_handler.check_password(password, hashed_password)
        if not is_correct_password: raise Exception('Password is incorrect')

    def __create_jwt_token(self, user_id: int) -> str:
        payload = { "user_id": user_id}
        token = self.__jwt_handler.create_jwt_token(payload)
        return token
    
    def __format_response(self, username: str, user_id: int, token: str) -> dict:
        return {
            "access": True,
            "username": username,
            "user_id": user_id,
            "token": token
        }