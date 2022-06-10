#!/usr/bin/python

import argparse
from configparser import ConfigParser

from Utils import get_users, get_roles
from db.DbUtils import DbUtils
from services.Idp import Idp
from services.Realm import Realm
from services.Users import Users

if __name__ == '__main__':

    # Чтение аргументов командной строки
    parser = argparse.ArgumentParser(description="User management util")
    parser.add_argument("--dry-run",
                        dest="dry_run",
                        help='Запуск в режиме проверки, без commit-а в БД',
                        action='store_true')
    parser.add_argument("--exclude-services",
                        nargs='+',
                        help='Список сервисов, которые нужно исключить в процессе выполнения скрипта',
                        required=False)
    args = parser.parse_args()
    print(f'Переданные аргументы командной строки {args}')

    # Установка режима dry-run
    DbUtils.dry_run = args.dry_run

    # Чтение конфига подключения к базам данных
    p = ConfigParser()
    p.read('database.ini')

    # Создание пулла коннекций БД
    dbs = DbUtils.get_db_set(p)

    # Чтение списков данных
    users = get_users()
    roles = get_roles()

    # Выполнение логики по каждому сервису
    if "users" not in args.exclude_services:
        Users.prepare(dbs["users"], users)

    if "idp" not in args.exclude_services:
        Idp.prepare(dbs["idp"], users)

    if "realm" not in args.exclude_services:
        Realm.prepare(dbs["realm"], users, roles)

    # Закрытие пулла коннекций БД
    DbUtils.close_db_set(dbs)
