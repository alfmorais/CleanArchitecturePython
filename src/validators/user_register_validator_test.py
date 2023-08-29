import pytest
from src.errors.types import HttpUnprocessableEntityError
from .user_register_validator import user_register_validator


class MockRequest:
    def __init__(self) -> None:
        self.json = None


@pytest.mark.parametrize(
    "payload,response",
    [
        (
            {
                "first_name": 123,
                "last_name": "Morais",
                "age": 23,
            },
            {"first_name": ["must be of string type"]}
        ),
        (
            {
                "first_name": None,
                "last_name": "Morais",
                "age": 23,
            },
            {"first_name": ["null value not allowed"]}
        ),
        (
            {
                "last_name": "Morais",
                "age": 23,
            },
            {"first_name": ["required field"]}
        ),
        (
            {
                "first_name": "Alfredo",
                "last_name": 1234,
                "age": 23,
            },
            {"last_name": ["must be of string type"]}
        ),
        (
            {
                "first_name": "Alfredo",
                "last_name": None,
                "age": 23,
            },
            {"last_name": ["null value not allowed"]}
        ),
        (
            {
                "first_name": "Alfredo",
                "age": 23,
            },
            {"last_name": ["required field"]}
        ),
        (
            {
                "first_name": "Alfredo",
                "last_name": "Neto",
                "age": "31",
            },
            {"age": ["must be of integer type"]}
        ),
        (
            {
                "first_name": "Alfredo",
                "last_name": "Neto",
                "age": None,
            },
            {"age": ["null value not allowed"]}
        ),
        (
            {
                "first_name": "Alfredo",
                "last_name": "Neto",
            },
            {"age": ["required field"]}
        ),
    ]
)
def test_user_register_validator(payload, response):
    request = MockRequest()
    request.json = payload

    with pytest.raises(HttpUnprocessableEntityError) as error:
        user_register_validator(request)

    assert error.value.status_code == 422
    assert error.value.message == response
