#pylint: disable=broad-exception-raised
from typing import Dict
from src.domain.use_cases.users_register import UserRegisterInterface
from src.data.interfaces.users_repositories import UsersRepositoryInterface
from src.errors.types import HttpBadRequestError


class UserRegister(UserRegisterInterface):

    def __init__(self, user_repository: UsersRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        self.__validate_name(first_name)
        self.__validate_name(last_name)
        self.__validate_age(age)
        self.__registry_user_informations(first_name, last_name, age)
        return self.__format_response(first_name, last_name, age)

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise HttpBadRequestError("Nome invalido para a cadastro")

        if len(first_name) > 18:
            raise HttpBadRequestError("Nome muito grande para a cadastro")

    @classmethod
    def __validate_age(cls, age: int) -> None:
        if not isinstance(age, int):
            raise HttpBadRequestError("Idade precisa ser um número")

    def __registry_user_informations(self, first_name: str, last_name: str, age: int):
        self.__user_repository.insert_user(
            first_name,
            last_name,
            age,
        )

    @classmethod
    def __format_response(cls, first_name: str, last_name: str, age: int) -> Dict:
        response = {
            "type": "Users",
            "count": 1,
            "attributes": {
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
            },
        }
        return response
