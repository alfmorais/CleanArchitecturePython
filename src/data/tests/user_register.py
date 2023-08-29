from typing import Dict


class UserRegisterSpy:
    def __init__(self) -> None:
        self.find_attributes = {}

    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        self.find_attributes["first_name"] = first_name

        return {
            "type": "Users",
            "count": 1,
            "attributes": {
                "first_name": first_name,
                "last_name": last_name,
                "age": age,
            },
        }
