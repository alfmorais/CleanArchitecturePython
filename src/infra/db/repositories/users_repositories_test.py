from .users_repositories import UsersRepositories


def test_insert_user():
    mocked_user = {
        "first_name": "first",
        "last_name": "last",
        "age": 15
    }

    user_repository = UsersRepositories()
    user_repository.insert_user(**mocked_user)
