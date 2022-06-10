#!/usr/bin/python

import json
from configparser import ConfigParser
from typing import List
import argparse

from db.DbUtils import DbUtils
from services.Idp import Idp
from services.Realm import Realm
from entitys.Role import Role
from entitys.User import User
from services.Users import Users

parser = argparse.ArgumentParser(description="User management util")
parser.add_argument("--dry-run", dest="dry_run", action='store_true')
args = parser.parse_args()
print(f'Переданные аргументы {args}')
DbUtils.dry_run = args.dry_run


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


if __name__ == '__main__':
    p = ConfigParser()
    p.read('database.ini')

    users = get_users()
    roles = get_roles()

    dbs = DbUtils.get_db_set(p)

    Users.prepare(dbs["users"], users)

    Idp.prepare(dbs["idp"], users)

    Realm.prepare(dbs["realm"], users, roles)

    DbUtils.close_db_set(dbs)
