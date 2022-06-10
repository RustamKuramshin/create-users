import argparse
import json
from argparse import Namespace
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


def get_command_line_args() -> Namespace:
    parser = argparse.ArgumentParser(description="User management util")
    parser.add_argument("--dry-run",
                        dest="dry_run",
                        help='Запуск в режиме проверки, без commit-а в БД',
                        action='store_true')
    parser.add_argument("--exclude-services",
                        nargs='+',
                        help='Список сервисов, которые нужно исключить в процессе выполнения скрипта',
                        required=False)

    return parser.parse_args()
