import json
from typing import List

from entitys.Role import Role
from entitys.User import User


def get_users() -> List[User]:
    users_list: List[User] = []
    users_json = json.load(open('users.json'))
    for u in users_json:
        user: User = User(**u)
        validate_user(user)
        users_list.append(user)

    return users_list


def validate_user(user: User):
    if (user.role_id is None) and (user.role_name is None):
        raise Exception("Роль пользователя и её id не могут быть одновременно null")


def get_roles() -> List[Role]:
    roles_list: List[Role] = []
    roles_json = json.load(open('roles.json'))
    for r in roles_json:
        roles_list.append(Role(**r))

    return roles_list
