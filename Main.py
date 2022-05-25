#!/usr/bin/python

import json
from configparser import ConfigParser
from typing import List

from DbUtils import DbUtils
from Idp import Idp
from User import User


def get_users() -> List[User]:
    users_list: List[User] = []
    users_json = json.load(open('users.json'))
    for u in users_json:
        users_list.append(User(**u))

    return users_list


if __name__ == '__main__':
    p = ConfigParser()
    p.read('database.ini')

    users = get_users()

    dbs = DbUtils.get_db_set(p)

    Idp.prepare(dbs["nn_idp"].cursor, users)

    DbUtils.close_db_set(dbs)
