from typing import List
import pytest
from src.domain.models.users import Users
from src.infra.db.tests.users_repositories import UsersRepositorySpy
from .user_finder import UserFinder


def test_user_finder_error_first_name_is_not_alpha():
    first_name = "100 Asilo"
    users_repository = UsersRepositorySpy()
    user_finder = UserFinder(users_repository)

    with pytest.raises(Exception) as error:
        user_finder.find(first_name)

    assert error.value.args[0] == "Nome invalido para a busca"


def test_user_finder_error_first_name_len_more_than_max_characters():
    first_name = "RedWackyLeagueAntlezBroketheStereoNeon"
    users_repository = UsersRepositorySpy()
    user_finder = UserFinder(users_repository)

    with pytest.raises(Exception) as error:
        user_finder.find(first_name)

    assert error.value.args[0] == "Nome muito grande para a busca"


def test_user_finder_error_first_name_not_found():
    class UsersRepositorySpyError(UsersRepositorySpy):
        def select_user(self, first_name: str) -> List[Users]:
            return []

    first_name = "Davi"
    users_repository = UsersRepositorySpyError()
    user_finder = UserFinder(users_repository)

    with pytest.raises(Exception) as error:
        user_finder.find(first_name)

    assert error.value.args[0] == "Usuario não encontrado"


def test_user_finder_success():
    first_name = "Joaquim"
    users_repository = UsersRepositorySpy()
    user_finder = UserFinder(users_repository)

    response = user_finder.find(first_name)

    assert response["type"] == "Users"
    assert response["count"] == 2
    assert response["attributes"] != []
