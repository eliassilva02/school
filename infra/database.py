import psycopg2 as pg

class DB:
    def __init__(self) -> None:
        self.conn = None
        self.cur = None        

    def open_connection(self):
        self.conn = pg.connect(
            dbname = '',
            port='',
            password = '',
            host = '',
            user = ''
        )

        self.cur = self.conn.cursor()

    def select(self, sql: str) -> list[tuple]:
        if self.cur.connection.closed != 0:
            self.open_connection()
        
        self.cur.execute(sql)

        return self.cur.fetchall()

    def manipulation(self, sql: str) -> None:
        if self.cur.connection.closed != 0:
            self.open_connection()
        
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()