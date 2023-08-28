#pylint: disable=broad-exception-raised
from typing import Dict
from src.domain.use_cases.users_finder import UserFinderInterface
from src.data.interfaces.users_repositories import UsersRepositoryInterface


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        """
        Regras:
        
        - first_name contendo números
        - first_name com mais de 18 letras
        - retornar erro em caso não encontre o usuário
        - formatar a resposta
        """
        if not first_name.isalpha():
            raise Exception("Nome invalido para a busca")

        if len(first_name) > 18:
            raise Exception("Nome muito grande para a busca")

        users = self.__users_repository.select_user(first_name)

        if users == []:
            raise Exception("Usuario não encontrado")

        response = {
            "type": "Users",
            "count": len(users),
            "attributes": users,
        }
        return response
