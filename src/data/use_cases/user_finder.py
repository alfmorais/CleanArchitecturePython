from typing import Dict
from src.domain.use_cases.users_finder import UserFinderInterface
from src.data.interfaces.users_repositories import UsersRepositoryInterface


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:
        return self.__users_repository.select_user(first_name)
