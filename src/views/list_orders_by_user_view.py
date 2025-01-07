from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface
from src.controllers.interfaces.list_orders_controller import ListOrdersControllerInterface



class ListOrderByUserView(ViewInterface):
    def __init__(self, controller: ListOrdersControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        # Get user_id from headers
        user_id = int(http_request.headers['uid'])
        print(type(user_id))
        # Verify if user_id is valid
        self.__validate_input(user_id)

        response = self.__controller.list_orders(user_id)

        return HttpResponse(body={"data": response}, status_code=200)

    def __validate_input(self, user_id: any) -> None:
        if (
            not user_id
            or not isinstance(user_id, int)
        ): raise Exception('Invalid input')
        