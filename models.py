import pymysql
import datetime
from util.DB import DB
from psycopg2 import IntegrityError

class dbConnect:
    def createUser(user):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO M_USER (id, user_name, email, password) VALUES (%s, %s, %s, %s);"
            cur.execute(sql, (user.id, user.name, user.email, user.password))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getUserId(name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT id FROM M_USER WHERE user_name=%s;"
            cur.execute(sql, (name))
            id = cur.fetchone()
            return id
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close


    def getUser(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM M_USER WHERE email=%s;"
            cur.execute(sql, (email))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close


    def getChannelAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM T_CHANNEL;"
            cur.execute(sql)
            channels = cur.fetchall()
            return channels
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getChannelById(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM T_CHANNEL WHERE id=%s;"
            cur.execute(sql, (cid))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM T_CHANNEL WHERE name=%s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def addChannel(uid, newChannelName, newChannelDescription):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO T_CHANNEL (uid, name, abstract) VALUES (%s, %s, %s);"
            cur.execute(sql, (uid, newChannelName, newChannelDescription))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM T_CHANNEL WHERE name=%s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
        except Exception as e:
            print(e + 'が発生しました')
            return None
        finally:
            cur.close()
            return channel


    def updateChannel(uid, newChannelName, newChannelDescription, cid):
        conn = DB.getConnection()
        cur = conn.cursor()
        sql = "UPDATE T_CHANNEL SET uid=%s, name=%s, abstract=%s WHERE id=%s;"
        cur.execute(sql, (uid, newChannelName, newChannelDescription, cid))
        conn.commit()
        cur.close()


    #deleteチャンネル関数
    def deleteChannel(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM T_CHANNEL WHERE id=%s;"
            cur.execute(sql, (cid))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getMessageAll(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT TM.id, MU.id as uid, user_name, message_contents, send_at FROM T_MESSAGE AS TM INNER JOIN M_USER AS MU ON TM.uid = MU.id WHERE cid = %s;"
            cur.execute(sql, (cid))
            messages = cur.fetchall()
            return messages
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def createMessage(uid, cid, message):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            send_at = datetime.datetime.now().strftime("%-m/%d %-H:%M")
            sql = "INSERT INTO T_MESSAGE(uid, cid, message_contents, send_at) VALUES(%s, %s, %s, %s)"
            cur.execute(sql, (uid, cid, message, send_at))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def addReaction(mid, uid, reaction_code):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO T_REACTION(mid, uid, reaction_code) VALUES(%s, %s, %s)"
            cur.execute(sql, (mid, uid, reaction_code))
            conn.commit()
        except IntegrityError as e:
            print(e + '一意制約違反')
            return None
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    def getReactionAll(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT TM.id, MU.id as uid, user_name, message_contents, TR.mid, TR.reaction_code, file_path, COUNT(*) as reaction_count  FROM M_USER AS MU INNER JOIN T_MESSAGE AS TM ON MU.id = TM.uid LEFT JOIN T_REACTION AS TR ON TM.id = TR.mid LEFT JOIN M_REACTION AS MR ON TR.reaction_code = MR.id WHERE cid = %s GROUP BY TM.id, MU.id, user_name, message_contents, TR.mid, TR.reaction_code, file_path;"
            cur.execute(sql, (cid))
            reactions = cur.fetchall()
            return reactions
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()

    def deleteMessage(mid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM T_MESSAGE WHERE id=%s;"
            cur.execute(sql, (mid))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()