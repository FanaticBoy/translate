from db import db_conn


class Login:
    def __init__(self):
        self.lianjie = db_conn.Connect_sql()

    def chaXunuser(self):
        with self.lianjie.conn.cursor() as c:
            sql = "select *from Users"
            ret = c.execute(sql)
            self.lianjie.conn.commit()
            self.duqu = c.fetchall()
            return self.duqu
