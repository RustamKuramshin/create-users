from psycopg2.extensions import connection
from psycopg2.extensions import cursor


class Db:
    connection: connection
    cursor: cursor
    db_name: str

    def __init__(self, db_name: str, conn: connection, cur: cursor):
        self.db_name = db_name
        self.connection = conn
        self.cursor = cur
