from src.presentation.controllers.user_finder_controller import UserFinderController
from src.presentation.http_types.http_response import HttpResponse
from src.data.tests.user_finder import UserFinderSpy


class HttpRequestMock():
    def __init__(self) -> None:
        self.query_params = {"first_name": "meu_teste"}


def test_handle_success():
    http_request = HttpRequestMock()
    use_case = UserFinderSpy()
    user_finder_controller = UserFinderController(use_case)

    response = user_finder_controller.handle(http_request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body == {
        "data": {
            "type": "Users",
            "count": 1,
            "attributes": [
                {
                    "first_name": http_request.query_params["first_name"],
                    "last_name": "something",
                    "age": 31,
                }
            ]
        }
    }
