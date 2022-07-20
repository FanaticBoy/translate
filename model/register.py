from db import db_conn


class Users:
    def __init__(self):
        self.lianjie = db_conn.Connect_sql()

    def add_user(self, name, passwd):
        with self.lianjie.conn.cursor() as c:
            sql = "INSERT into Users VALUES(%s,%s)"
            ret = c.execute(sql, args=(name, passwd))
            self.lianjie.conn.commit()