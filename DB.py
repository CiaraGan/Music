# Python 3
import pymysql


def All_Songs():
    # 打开数据库连接
    db = pymysql.connect("127.0.0.1", "Ciara", "Ciara", "Music")
    # 使用 cursor() 方法创建一个游标对象 cursor
    Cur1 = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    Cur1.execute("SELECT Song_Name FROM Music.Songs_List")

    # 使用 fetchone() 方法获取单条数据.
    Result1 = Cur1.fetchall()
    Cur1.close()
    # 关闭数据库连接
    db.close()
    return Result1

def Delete_Song_In_Db(Song_Name):
    db = pymysql.connect("127.0.0.1", "Ciara", "Ciara", "Music")
    Cur1 = db.cursor()
    sql = "Delete  FROM Music.Songs_List Where Song_Name='" + Song_Name + "'"
    try:
        Cur1.execute(sql)
        print(sql)
    except:
        print("Delete failed!")
    else:
        print("Delete Success!")
    print(sql)
    Cur1.close()
    db.commit()
    db.close()
    return ""


