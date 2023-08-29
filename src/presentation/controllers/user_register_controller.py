from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.users_register import UserRegisterInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class UserRegisterController(ControllerInterface):

    def __init__(self, use_cases: UserRegisterInterface) -> None:
        self.__use_cases = use_cases

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        params = http_request.body
        response = self.__use_cases.register(**params)

        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
