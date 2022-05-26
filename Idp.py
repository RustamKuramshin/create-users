from typing import List

from Db import Db
from User import User


class Idp:
    @staticmethod
    def prepare(db: Db, users: List[User]):
        sql_insert_identity = """INSERT INTO identity (user_id, realm_id, email, password_hash) 
                             VALUES (%s, %s, %s, %s)"""

        for user in users:
            db.cursor.execute(sql_insert_identity, (user.user_id, user.realm_id, user.email, user.password_hash))

        db.connection.commit()
