from src.presentation.controllers.user_register_controller import UserRegisterController
from src.presentation.http_types.http_response import HttpResponse
from src.data.tests.user_register import UserRegisterSpy


class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = {"first_name": "meu_teste"}
        self.body = {
            "first_name": "Alfredo",
            "last_name": "Morais",
            "age": 31,
        }


def test_handle_success():
    http_request = HttpRequestMock()
    use_case = UserRegisterSpy()
    user_finder_controller = UserRegisterController(use_case)

    response = user_finder_controller.handle(http_request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body == {
        "data": {
            "type": "Users",
            "count": 1,
            "attributes": {
                "first_name": http_request.body["first_name"],
                "last_name": http_request.body["last_name"],
                "age": http_request.body["age"],
            },
        }
    }
