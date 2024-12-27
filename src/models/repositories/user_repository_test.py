""" from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.user_repository import UserRepository

# teste de integração
def test_user_repository():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    repo = UserRepository(conn)

    username = "user_test"
    password = "12345"
    email = "test@test.com"

    user = repo.create_user(username, password, email)

    print()
    print(user) """