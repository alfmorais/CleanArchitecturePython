from src.infra.db.repositories.users_repositories import UsersRepository
from .user_finder import UserFinder


def test_user_finder():
    users_repository = UsersRepository()
    user_finder = UserFinder(users_repository)

    assert user_finder is not None
