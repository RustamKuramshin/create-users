from typing import List

from db.Db import Db
from db.DbUtils import DbUtils
from entitys.Role import Role
from entitys.User import User


class Realm:
    @staticmethod
    def prepare(db: Db, users: List[User], roles: List[Role]):
        print('Подготовка REALM')

        sql_insert_user_realm_role = """INSERT INTO user_realm_role (realm_id, user_id, role_id)
                                        VALUES (%s, %s, %s)"""

        sql_insert_role = """INSERT INTO roles (role_id, name, realm_id) VALUES (%s, %s, %s)"""

        for role in roles:
            if not DbUtils.is_record_exist(db, "roles", "name", role.name):
                db.cursor.execute(sql_insert_role, (role.role_id, role.name, role.realm_id))
                # role.role_id = int(db.cursor.fetchone()[0])
                Role.role_name_to_id[role.name] = role.role_id

        for user in users:
            if not DbUtils.is_record_exist(db, "user_realm_role", "user_id", user.user_id):
                if (user.role_id is None) and (user.role_name in Role.role_name_to_id):
                    user.role_id = Role.role_name_to_id[user.role_name]
                db.cursor.execute(sql_insert_user_realm_role, (user.realm_id, user.user_id, user.role_id))
                print('Вставлен юзер - {}'.format(user))

        DbUtils.alter_sequence(db, "realm", "realm_id")
        DbUtils.alter_sequence(db, "realm_resource", "resource_id")
        DbUtils.alter_sequence(db, "roles", "role_id")

        DbUtils.commit(db)
