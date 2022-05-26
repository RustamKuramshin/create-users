from typing import List

from Db import Db
from User import User


class Realm:
    @staticmethod
    def prepare(db: Db, users: List[User]):
        sql_insert_user_realm_role = """INSERT INTO user_realm_role (realm_id, user_id, role_id)
                                        VALUES (%s, %s, %s)"""

        for user in users:
            db.cursor.execute(sql_insert_user_realm_role, (user.realm_id, user.user_id, user.role_id))

        db.connection.commit()
