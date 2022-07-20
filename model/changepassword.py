from db import db_conn


class Change:
    def __init__(self):
        self.lianjie = db_conn.Connect_sql()

    def change_user(self,  passwd,name):
        with self.lianjie.conn.cursor() as c:
            sql = "update Users set u_password=(%s) where u_name=(%s)"
            ret = c.execute(sql, args=(passwd, name))
            self.lianjie.conn.commit()

if __name__ == '__main__':
    change = Change()
    change.change_user("14234")