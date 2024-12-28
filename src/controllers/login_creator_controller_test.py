""" from src.models.repositories.user_repository import UserRepository
from src.controllers.login_creator_controller import LoginCreatorController
from src.models.settings.db_connection_handler import db_connection_handler

def test_login_creator_controller():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)
    controller = LoginCreatorController(repo)

    username = "user_test_controller"
    password = "12345"


    response = controller.create(username, password)

    print()
    print(response) """