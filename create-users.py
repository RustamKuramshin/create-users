#!/usr/bin/python

from Utils import get_users, get_roles, get_command_line_args
from db.DbUtils import DbUtils
from services.Idp import Idp
from services.Realm import Realm
from services.Users import Users

if __name__ == '__main__':

    # Чтение аргументов командной строки
    args = get_command_line_args()
    print(f'Переданные аргументы командной строки {args}')

    # Установка режима dry-run
    DbUtils.dry_run = args.dry_run

    # Создание пулла коннекций БД
    dbs = DbUtils.get_db_set('database.ini')

    # Чтение списков входных данных
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
