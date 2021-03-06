from typing import List

from db.Db import Db
from db.DbUtils import DbUtils
from entitys.User import User


class Idp:
    @staticmethod
    def prepare(db: Db, users: List[User]):
        print("Подготовка IDP")
        sql_insert_identity = """INSERT INTO identity (user_id, realm_id, email, password_hash) 
                             VALUES (%s, %s, %s, %s)"""

        for user in users:
            if not DbUtils.is_record_exist(db, "identity", "user_id", user.user_id):
                db.cursor.execute(sql_insert_identity, (user.user_id, user.realm_id, user.login, user.password_hash))
                print('Вставлен юзер - {}'.format(user))

        DbUtils.alter_sequence(db, "identity", "user_id")

        DbUtils.commit(db)
