import pytest
from src.errors.types import HttpUnprocessableEntityError
from .user_finder_validator import user_finder_validator


class MockRequest:
    def __init__(self) -> None:
        self.args = None


@pytest.mark.parametrize(
    "first_name,response",
    [
        (
            {"first_name": 123},
            {"first_name": ["must be of string type"]}
        ),
        (
            {"first_name": None},
            {"first_name": ["null value not allowed"]}
        ),
        (
            {},
            {"first_name": ["required field"]}
        ),
    ]
)
def test_user_finder_validator(first_name, response):
    request = MockRequest()
    request.args = first_name

    with pytest.raises(HttpUnprocessableEntityError) as error:
        user_finder_validator(request)

    assert error.value.status_code == 422
    assert error.value.message == response
