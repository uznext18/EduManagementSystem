import json
import re

from v1.common import UserRole


class File:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def read(self) -> dict:
        with open(f"/home/user/PycharmProjects/lesson_8/HomeWork/EduManagementSystem/DB/{self.file_name}", 'r') as f:
            return json.load(f)

    def write(self, data: dict) -> None:
        with open(f"/home/user/PycharmProjects/lesson_8/HomeWork/EduManagementSystem/DB/{self.file_name}", 'w') as f:
            json.dump(data, f, indent=4)


def sequence_id() -> int:
    file: File = File('users.json')
    users: list = list(file.read().keys())
    if users:
        return int(users[-1]) + 1
    return 1


def get_all() -> dict:
    file: File = File('users.json')
    users: dict = file.read()
    return users


class User:
    def __init__(self, id: int = None, username: str = None, email: str = None, password: str = None,
                 role: str = UserRole.GUEST.value, join_date: str = None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.join_date = join_date

    def save(self) -> None:
        self.validate_login()
        file: File = File('users.json')
        users: dict = file.read()
        for u in list(users.values()):
            if u['email'] == self.email:
                raise Exception('The user with this email already exists')
        user: dict = {self.id: self.__dict__}
        users.update(user)
        file.write(users)

    def delete(self) -> None:
        file: File = File('users.json')
        users: dict = file.read()
        del users[str(self.id)]
        file.write(users)

    def get(self) -> dict:
        file: File = File('users.json')
        users: dict = file.read()
        user: dict = users[str(self.id)]
        return user

    def has_login(self):
        file: File = File('users.json')
        users: list = list(file.read().values())
        for user in users:
            if user['username'] == self.username and user['password'] == self.password:
                # print(user)
                # print(self.__dict__)
                return user
        raise Exception("The user not in the database.")

    def validate_login(self):
        if not re.match("^[a-z0-9_-]{3,15}$", self.username):
            raise Exception("The username isn't strong.")
        if not re.match("[^@ \t\r\n]+@[^@ \t\r\n]+[^@ \t\r\n]+", self.email):
            raise Exception("The email address isn't strong.")
        if not re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$", self.password):
            raise Exception("The password isn't strong.")
