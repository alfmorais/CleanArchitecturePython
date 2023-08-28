import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from .users_repositories import UsersRepository


db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason="Sensive Test")
def test_insert_user():
    mocked_user = {
        "first_name": "first",
        "last_name": "last",
        "age": 15
    }

    user_repository = UsersRepository()
    user_repository.insert_user(**mocked_user)

    sql = """
        SELECT * FROM users
        WHERE first_name = '{}'
        AND last_name = '{}'
        AND age = '{}'
    """.format(
        mocked_user["first_name"],
        mocked_user["last_name"],
        mocked_user["age"]
    )

    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.first_name == mocked_user["first_name"]
    assert registry.last_name == mocked_user["last_name"]
    assert registry.age == mocked_user["age"]

    connection.execute(
        text(
            f"""DELETE FROM users WHERE id = {registry.id}"""
        )
    )
    connection.commit()


@pytest.mark.skip(reason="Sensive Test")
def test_select_user():
    mocked_user = {
        "first_name": "first",
        "last_name": "last",
        "age": 15
    }

    sql = """
        INSERT INTO users (first_name, last_name, age) VALUES ('{}', '{}', '{}')
    """.format(
        mocked_user["first_name"],
        mocked_user["last_name"],
        mocked_user["age"]
    )
    connection.execute(text(sql))
    connection.commit()

    user_repository = UsersRepository()
    response = user_repository.select_user(mocked_user["first_name"])

    assert response[0].first_name == mocked_user["first_name"]
    assert response[0].last_name == mocked_user["last_name"]
    assert response[0].age == mocked_user["age"]

    connection.execute(
        text(
            f"""DELETE FROM users WHERE id = {response[0].id}"""
        )
    )
    connection.commit()
