from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.interfaces.create_orders_controller import CreateOrdersControllerInterface
from src.views.interfaces.view_interface import ViewInterface

class CreateOrdersView(ViewInterface):
    def __init__(self, controller: CreateOrdersControllerInterface):
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.headers['uid']
        description = http_request.body['description']
        self.__validate_inputs(user_id, description)

        response = self.__controller.create(user_id, description)

        return HttpResponse(body={"data": response }, status_code=201)
    
    def __validate_inputs(self, user_id: int, description: str) -> None:
        if (
            not description
            or not user_id
        ): raise Exception("Invalid input")
