from pymysql import Connect
class Connect_sql:
    def __init__(self):
        self.conn = Connect(host='自己数据库主机', port=数据库端口, user='root', passwd='自己密码', db='users')
if __name__ == '__main__':
    sql = Connect_sql()
