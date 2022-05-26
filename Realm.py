from typing import List

from Db import Db
from DbUtils import DbUtils
from User import User


class Realm:
    @staticmethod
    def prepare(db: Db, users: List[User]):
        print('Подготовка REALM')
        sql_insert_user_realm_role = """INSERT INTO user_realm_role (realm_id, user_id, role_id)
                                        VALUES (%s, %s, %s)"""

        for user in users:
            if not DbUtils.is_record_exist(db, "user_realm_role", "user_id", user.user_id):
                db.cursor.execute(sql_insert_user_realm_role, (user.realm_id, user.user_id, user.role_id))
                print('Вставлен юзер - {}'.format(user))

        db.connection.commit()
