from configparser import ConfigParser
from typing import Dict

import psycopg2
from psycopg2.extras import RealDictCursor

from Db import Db


class DbUtils:
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
    def is_record_exist(db: Db, table: str, column: str, record_id: int) -> bool:
        sql_select = 'SELECT * FROM {table} t WHERE t.{column} = %s'.format(table=table, column=column)
        print(sql_select)
        db.cursor.execute(sql_select, [record_id])
        rows = db.cursor.fetchall()
        res = len(rows) == 1

        if res:
            print(f'В таблице {table} найдена запись с record_id {record_id}'.format(table=table, record_id=record_id))
        else:
            print(
                f'В таблице {table} НЕ найдена запись с record_id {record_id}'.format(table=table, record_id=record_id))

        return res
