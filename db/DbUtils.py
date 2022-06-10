from configparser import ConfigParser
from typing import Dict

import psycopg2
from psycopg2.extras import RealDictCursor

from db.Db import Db


class DbUtils:

    dry_run: bool

    @staticmethod
    def get_db_config(db_name, parser: ConfigParser):
        db = {}
        if parser.has_section(db_name):
            params = parser.items(db_name)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found'.format(db_name))
        return db

    @staticmethod
    def get_db_set(parser: ConfigParser) -> Dict[str, Db]:
        db_set: Dict[str, Db] = {}
        try:
            for section in parser.sections():
                print('Connecting to {}'.format(section))
                conn = psycopg2.connect(**DbUtils.get_db_config(section, parser))
                db_set[section] = Db(db_name=section, conn=conn, cur=conn.cursor(cursor_factory=RealDictCursor))
            return db_set
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    @staticmethod
    def close_db_set(db_set: Dict[str, Db]):
        for db in db_set.values():
            print('Close connection to {}'.format(db.db_name))
            conn = db.connection
            if conn is not None:
                conn.close()

    @staticmethod
    def is_record_exist(db: Db, table: str, column: str, value) -> bool:
        sql_select = 'SELECT * FROM {table} t WHERE t.{column} = %s'.format(table=table, column=column)
        print(sql_select)
        db.cursor.execute(sql_select, [value])
        rows = db.cursor.fetchall()
        res = len(rows) == 1

        if res:
            print(f'В таблицу {table} НЕ будет добавлена запись с value {value}'.format(table=table, value=value))
        else:
            print(
                f'В таблицу {table} будет добавлена запись с value {value}'.format(table=table, value=value))

        return res

    @staticmethod
    def get_table_max_pk_id(db: Db, table: str, column: str) -> int:
        sql_select = 'SELECT max({column}) FROM {table}'.format(column=column, table=table)
        print(sql_select)
        db.cursor.execute(sql_select)
        max_id = int(db.cursor.fetchall()[0]['max'])

        print(f'Последний id поля {column} в таблице {table} равен {max_id}')

        return max_id

    @staticmethod
    def alter_sequence(db: Db, table: str, column: str):

        last_id = DbUtils.get_table_max_pk_id(db, table, column)

        sql_alter_sequence = 'ALTER SEQUENCE {seq} RESTART WITH {last_id}'.format(
            seq=f'{table}_{column}_seq',
            last_id=last_id
        )

        print(sql_alter_sequence)

        db.cursor.execute(sql_alter_sequence)

    @staticmethod
    def commit(db: Db):
        if DbUtils.dry_run:
            db.connection.rollback()
        else:
            db.connection.commit()

