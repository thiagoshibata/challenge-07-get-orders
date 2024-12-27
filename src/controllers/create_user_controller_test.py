""" from src.models.repositories.user_repository import UserRepository
from src.controllers.create_user_controller import CreateUserController
from src.models.settings.db_connection_handler import db_connection_handler

def test_create_user_controller():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)
    controller = CreateUserController(repo)

    username = "user_test_controller"
    password = "12345"
    email = "teste2@test.com"

    response = controller.create(username, password, email)

    print()
    print(response) """