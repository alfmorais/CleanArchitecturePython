import pytest
from src.infra.db.tests.users_repositories import UsersRepositorySpy
from .user_register import UserRegister


def test_register_user_success():
    first_name = "Alfredo"
    last_name = "Morais"
    age = 31

    repository = UsersRepositorySpy()
    user_register = UserRegister(repository)

    response = user_register.register(
        first_name,
        last_name,
        age,
    )

    assert response["type"] == "Users"
    assert response["count"] == 1
    assert response["attributes"]["first_name"] == first_name
    assert response["attributes"]["last_name"] == last_name
    assert response["attributes"]["age"] == age


def test_user_register_error_first_name_is_not_alpha():
    first_name = "100 Asilo"
    last_name = "Morais"
    age = 31

    users_repository = UsersRepositorySpy()
    user_register = UserRegister(users_repository)

    with pytest.raises(Exception) as error:
        user_register.register(
            first_name,
            last_name,
            age,
        )

    assert error.value.args[0] == "Nome invalido para a busca"


def test_user_register_error_first_name_len_more_than_max_characters():
    first_name = "RedWackyLeagueAntlezBroketheStereoNeon"
    last_name = "Morais"
    age = 31

    users_repository = UsersRepositorySpy()
    user_register = UserRegister(users_repository)

    with pytest.raises(Exception) as error:
        user_register.register(
            first_name,
            last_name,
            age,
        )

    assert error.value.args[0] == "Nome muito grande para a busca"


def test_user_register_error_last_name_is_not_alpha():
    first_name = "Asilo"
    last_name = "100 Morais"
    age = 31

    users_repository = UsersRepositorySpy()
    user_register = UserRegister(users_repository)

    with pytest.raises(Exception) as error:
        user_register.register(
            first_name,
            last_name,
            age,
        )

    assert error.value.args[0] == "Nome invalido para a busca"


def test_user_register_error_last_name_len_more_than_max_characters():
    first_name = "Morais"
    last_name = "RedWackyLeagueAntlezBroketheStereoNeon"
    age = 31

    users_repository = UsersRepositorySpy()
    user_register = UserRegister(users_repository)

    with pytest.raises(Exception) as error:
        user_register.register(
            first_name,
            last_name,
            age,
        )

    assert error.value.args[0] == "Nome muito grande para a busca"


def test_user_register_error_validate_age():
    first_name = "Morais"
    last_name = "Morais"
    age = "31"

    users_repository = UsersRepositorySpy()
    user_register = UserRegister(users_repository)

    with pytest.raises(Exception) as error:
        user_register.register(
            first_name,
            last_name,
            age,
        )

    assert error.value.args[0] == "Idade precisa ser um número"
