from pymysql import Connect
class Connect_sql:
    def __init__(self):
        self.conn = Connect(host='sh-cynosdbmysql-grp-78qgbl24.sql.tencentcdb.com', port=21087, user='root', passwd='ZHLsk153150274@', db='users')
if __name__ == '__main__':
    sql = Connect_sql()