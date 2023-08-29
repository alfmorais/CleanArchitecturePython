from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.users_finder import UserFinderInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class UserFinderController(ControllerInterface):

    def __init__(self, use_cases: UserFinderInterface) -> None:
        self.__use_cases = use_cases

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.query_params["first_name"]
        response = self.__use_cases.find(first_name)

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
