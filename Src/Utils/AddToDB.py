


import pymysql
from time import sleep
from utils import LoggingPrint
from DBUtils.PooledDB import PooledDB # 数据库连接池

log = LoggingPrint

# 1.查询操作
def searchDB():
    db = pymysql.connect(
        host="106.14.171.39",
        user="root",
        password="123456",
        db="dds",
        port=3306,
        charset='utf8'
    )

    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    sql = "select * from amazon"
    try:
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        print("amazon——table")
        for row in results:
            id = row[0]
            url_type = row[1]
            Bookname = row[2]
            Bookprice = row[3]
            CreatTime = row[4]
            print('id =',id,'，url_type =',url_type, '，Bookname =',Bookname,'，Bookprice =',Bookprice,'，CreatTime =',CreatTime)
    except Exception as e:
        raise e
    finally:
        db.close()  # 关闭连接

'''
    参数说明：
            1. 书网分类（amazon/dangdang）  2. 图书名字
            3. 图书价格                    4.创建时间
            5. 评论数                      6.评星
            7. ISBN                       8.包装类型 （精装/平装）
            9. 图书分类 (综合/文学/科技)     10.日排行榜
'''
# 2.插入数据
def addMessageDB(Bookurl_type_s,Bookname_s,
                 Bookprice_s,CreatTime_s,
                 Comment_amount_s,Star_s,
                 ISBN_s,Package_s,
                 BookType_s,DayTop_s):

    db = pymysql.connect(
        host="106.14.171.39",
        user="root",
        password="123456",
        db="dds",
        port=3306,
        charset='utf8'
    )

    pool = PooledDB(pymysql, 10, host=db.host, user=db.user, passwd=db.password, db=db.db, port=db.port,charset="utf8")  # 5为连接池里的最少连接数
    conn = pool.connection()
    # 使用cursor()方法获取操作游标
    cur = conn.cursor()

    if(Bookurl_type_s == 'amazon'):
        sql_insert = "insert into amazon(url_type,Bookname,Bookprice,CreatTime,Comment_amount,Star,ISBN,Package,BookType,DayTop) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    elif(Bookurl_type_s == 'dangdang'):
        sql_insert = "insert into dangdang(url_type,Bookname,Bookprice,CreatTime,Comment_amount,Star,ISBN,Package,BookType,DayTop) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    elif(Bookurl_type_s == 'JD'):
        sql_insert = "insert into jd(url_type,Bookname,Bookprice,CreatTime,Comment_amount,Star,ISBN,Package,BookType,DayTop) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    else:
        print('查无此表')
    try:

        # cur.execute(sql_insert,(Bookurl_type_s,Bookname_s,Bookprice_s,CreatTime_s,
        #                         Comment_amount_s,Star_s,ISBN_s,Package_s,BookType_s,DayTop_s))
        # # 提交
        # db.commit()

        r = cur.execute(sql_insert,(Bookurl_type_s,Bookname_s,Bookprice_s,CreatTime_s,
                                Comment_amount_s,Star_s,ISBN_s,Package_s,BookType_s,DayTop_s))
        conn.commit()

        message_str = '{0}_{1}_{2}'.format(BookType_s,DayTop_s,'提交成功')
        log.logInfo(message_str)
        sleep(2)
        return r
    except Exception as e:
        # 错误回滚
        log.logInfo(e)
        db.rollback()
        # log.logError('提交失败')
    finally:
        # db.close()
        cur.close()
        conn.close()

# def closeDB():
#     print('sql链接关闭')
#     db.close()


if __name__ == '__main__':
    Bookurl_type = 'amazon'
    url_type_s = 'amazon_2'
    Bookname_s = 'D你好DS——book'
    Bookprice_s = 99.99
    CreatTime_s = '2018-04-07 00:00:00'
    addMessageDB(Bookurl_type,url_type_s,Bookname_s,Bookprice_s,CreatTime_s)








