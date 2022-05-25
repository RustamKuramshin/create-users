from typing import List

from psycopg2.extensions import cursor

from User import User


class Idp:
    @staticmethod
    def prepare(idp: cursor, users: List[User]):
        idp.execute('SELECT * FROM identity')
        print(idp.description)
        ids = idp.fetchall()
        for i in ids:
            print(i['email'])

