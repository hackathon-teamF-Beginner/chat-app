import pymysql

class DB:
    def getConnection():
        try:
            conn = pymysql.connect(
            host="neeeeche0526-rds.cz14wf3xiumc.ap-northeast-1.rds.amazonaws.com",
            db="chatapp",
            user="megane",
            password="meganemama",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()
