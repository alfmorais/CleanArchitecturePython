#pylint: disable=broad-exception-raised
from typing import Dict, List
from src.domain.use_cases.users_finder import UserFinderInterface
from src.data.interfaces.users_repositories import UsersRepositoryInterface
from src.domain.models.users import Users
from src.errors.types import HttpNotFoundError, HttpBadRequestError


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        self.__validate_name(first_name)
        users = self.__search_user(first_name)
        return self.__format_response(users)

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise HttpBadRequestError("Nome invalido para a busca")

        if len(first_name) > 18:
            raise HttpBadRequestError("Nome muito grande para a busca")

    def __search_user(self, first_name: str) -> List[Users]:
        users = self.__users_repository.select_user(first_name)

        if users == []:
            raise HttpNotFoundError("Usuario não encontrado")

        return users

    @classmethod
    def __format_response(cls, users: List[Users]) -> Dict:
        attributes = []

        for user in users:
            attributes.append(
                {
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "age": user.age,
                }
            )

        response = {
            "type": "Users",
            "count": len(attributes),
            "attributes": attributes,
        }
        return response
