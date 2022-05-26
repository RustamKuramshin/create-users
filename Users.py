from typing import List
from datetime import datetime

from Db import Db
from DbUtils import DbUtils
from User import User


class Users:
    @staticmethod
    def prepare(db: Db, users: List[User]):
        print('Подготовка USERS')
        sql_insert_user_info = """INSERT INTO user_info (user_id, realm_id, user_name, user_surname, user_patronymic, user_phone) 
                                  VALUES (%s, %s, %s, %s, %s, %s)"""

        sql_insert_user_photo = """INSERT INTO user_photo (user_id, realm_id, file_name, file_extension, photo_s3_key, size, height, width, ratio, created_at) 
                                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        for user in users:
            if not DbUtils.is_record_exist(db, "user_info", "user_id", user.user_id):
                db.cursor.execute(sql_insert_user_info, (
                    user.user_id, user.realm_id, user.user_name, user.user_surname, user.user_patronymic, user.user_phone))
            print('Вставлено info юзера - {}'.format(user))

            if not DbUtils.is_record_exist(db, "user_photo", "user_id", user.user_id):
                db.cursor.execute(sql_insert_user_photo,
                                  (user.user_id, user.realm_id, "", "", "", 0, 0, 0, 0, datetime.now()))

            print('Вставлено photo юзера - {}'.format(user))

        db.connection.commit()
