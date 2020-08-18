
import pymysql
from time import sleep
from utils import LoggingPrint
from DBUtils.PooledDB import PooledDB # 数据库连接池

log = LoggingPrint

mysqlInfo = pymysql.connect(
    host="106.14.171.39",
    user="root",
    password="123456",
    db="dds",
    port=3306,
    charset='utf8'
)

class OPMysql(object):


    __pool = None

    def __init__(self):
        # 构造函数，创建数据库连接、游标
        self.conn = OPMysql.getmysqlconn()
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)


    # 数据库连接池连接
    @staticmethod
    def getmysqlconn():
        if OPMysql.__pool is None:
            while True:
                try:
                    __pool = PooledDB(creator=pymysql, mincached=10, maxcached=100, host=mysqlInfo.host, user=mysqlInfo.user, passwd=mysqlInfo.password, db=mysqlInfo.db, port=mysqlInfo.port, charset=mysqlInfo.charset)
                    # print(__pool)
                    break
                except:
                    log.logInfo("尝试重连接失败0")
                    sleep(2)
                    continue
        return __pool.connection()


    # Demo_插入\更新\删除sql
    def op_insert(self, sql):
        insert_num = self.cur.execute(sql)
        self.conn.commit()
        return insert_num

    # Demo_查询
    def op_select(self, sql):
        self.cur.execute(sql)  # 执行sql
        select_res = self.cur.fetchone()  # 返回结果为字典
        return select_res

    # 释放资源
    def dispose(self):
        self.conn.close()
        self.cur.close()


    # 插入书籍详情数据
    def addMessageDB(self,Bookurl_type_s, Bookname_s,
                     Bookprice_s, CreatTime_s,
                     Comment_amount_s, Star_s,
                     ISBN_s, Package_s,
                     BookType_s, DayTop_s):


        if (Bookurl_type_s == 'amazon'):
            sql_insert = "insert into amazon(url_type,Bookname,Bookprice,CreatTime,Comment_amount,Star,ISBN,Package,BookType,DayTop) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        elif (Bookurl_type_s == 'dangdang'):
            sql_insert = "insert into dangdang(url_type,Bookname,Bookprice,CreatTime,Comment_amount,Star,ISBN,Package,BookType,DayTop) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        elif (Bookurl_type_s == 'JD'):
            sql_insert = "insert into jd(url_type,Bookname,Bookprice,CreatTime,Comment_amount,Star,ISBN,Package,BookType,DayTop) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        else:
            log.logInfo('Bookurl_type_s 参数错误')

        try: # 超时重连超过10秒后 报错
            i = 0
            while i<5:
                try:
                    i+=1
                    if i==5:
                        log.logError('插入失败 超时10秒');
                        break
                    else:
                        r = self.cur.execute(sql_insert, (Bookurl_type_s, Bookname_s, Bookprice_s, CreatTime_s,
                                                          Comment_amount_s, Star_s, ISBN_s, Package_s, BookType_s,
                                                          DayTop_s))
                        self.conn.commit()
                        message_str = '{0}_{1}_{2}'.format(BookType_s, DayTop_s, '插入成功')
                        log.logInfo(message_str)
                        return r
                        break
                except Exception as e:
                    message = '{0}_{1}'.format('插入数据——尝试重连', e)
                    log.logInfo(message)
                    self.conn = OPMysql.getmysqlconn()
                    self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
                    sleep(2)
        except Exception as e:
            # 错误回滚
            log.logInfo(e)
            mysqlInfo.rollback()



if __name__ == '__main__':
    #申请资源
    opm = OPMysql()

    sql = "select * from demo where name ='a' and pwd='e10adc3949ba59abbe56e057f20f883e' "
    res = opm.op_select(sql)

    #释放资源
    opm.dispose()







