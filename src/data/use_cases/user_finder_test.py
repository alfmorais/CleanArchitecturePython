import pytest
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
    first_name = "Davi"
    users_repository = UsersRepositorySpy()
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
