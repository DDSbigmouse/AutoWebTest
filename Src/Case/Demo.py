# coding: utf-8
#!/bin/sh
#. /etc/profile
#. ~/.bash_profile



from selenium import webdriver
from time import sleep
from BookMessage import AmazonBM
import time
import os
from utils import LoggingPrint
from pyvirtualdisplay import Display
from utils import OPMysql

Log = LoggingPrint
Server_mode = True # 服务器模式 需要置True

Url_book = 'https://www.amazon.cn/gp/bestsellers/books/ref=sv_b_3'
# print (os.getcwd()) # 打印当前路径


# 驱动配置
def driverStart():

    if (Server_mode == True):
        # 虚拟Xvfb窗口
        print('Xvfb')

        display = Display(visible=0, size=(1200, 960))
        display.start()

        if webdriver.Chrome() != None:
            driver = webdriver.Chrome()
            # driver = webdriver.Chrome(executable_path=os.getcwd() +'/dev/SkyEye/implement/LinuxDriver/chromedriver')  # Linux版
            # driver = webdriver.Chrome(executable_path=Path_linuxdriver)  # Linux版
        else:
            print('chromedriver 不存在')
        dr_list=[driver,display]
    else:
        # 客户端selenium窗口
        print('GUI')
        # driver = webdriver.Chrome(executable_path=os.getcwd()+'/utils/chromedriver') # 本地GUI
        driver = webdriver.Chrome(executable_path=os.getcwd() + '/implement/utils/chromedriver')  # Mac版
        dr_list = [driver]
    driver.get(Url_book)

    return dr_list

# 获取详情 并插入
def GetAllMessage(driver):
        print('——————————————AmazonMessage Get start——————————————')
        '''
        逻辑
        一.按分类按钮 字段获取:  1.书网分类（amazon）Add固定字段  2. 图书分类(综/文/科) Add固定字段(1,4,9 固定字段) 3.创建时间(固定字段)
        二.销量榜列表，字段获取： 1.获取销量榜List 
        三.根据销量榜List 遍历点击图书详情    
        四.判断是否电子书 -> 分别获取详情   字段获取:  
            字段顺序说明：
                    1. 书网分类  (固定字段)         2. 图书名字 
                    3. 图书价格                    4.创建时间   (固定字段) 
                    5. 评论数                      6.评星
                    7. ISBN                       8.包装类型 
                    9. 图书分类  (固定字段)         10.日排行榜
                        1.Bookurl_type_s,                 2.Bookname_s,
                        3.Bookprice_s,                    4.CreatTime_s,
                        5.Comment_amount_s,               6.Star_s,
                        7.ISBN_s,                         8.Package_s,
                        9.BookType_s,                    10.DayTop_s
        '''
        # 初始化对象
        AA = AmazonBM.AmazonMg

        # 一：1.书网分类 2.图书分类 3.创建时间
        Bookurl_type_s =  AA.Bookurl_type
        BookType_s = AA.BookType(driver)
        nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # 三: 详情爬取
        def InToDetails(i,b,opm):
            # 判断电子书标签
            nor_book = AA.JudeEBook(driver)
            if nor_book == '非电子书':
                # 图书名字
                Bookname_s = AA.getBookname(driver)
                # 包装类型
                Package_s = AA.getPackageType(driver)
                # 评星
                Star_s = AA.getStar(driver)
                # 评论数
                Comment_amount_s = AA.getComment_amount(driver)
                # 价格
                Bookprice_s = b
                # ISBN_list
                ISBN_list = AA.getISBNlist(driver)

                # 根据ISBN 数量 插表
                for ISBN_arr in ISBN_list:
                    if 'ISBN' in ISBN_arr.text: # 重要 判断ISBN字段
                        ISBN_arr_new = ISBN_arr.text.replace('ISBN: ', '') # 字符过滤
                        a = ISBN_arr_new.split(", ")        #
                        for num,ISBN_s in enumerate(a):
                            # 插表
                            # print(Bookurl_type_s,Bookname_s,Bookprice_s,nowtime,
                            #                      Comment_amount_s,Star_s,ISBN_s,Package_s,BookType_s,i)
                            opm.addMessageDB(Bookurl_type_s,Bookname_s,Bookprice_s,nowtime,
                                                 Comment_amount_s,Star_s,ISBN_s,Package_s,BookType_s,i)
                print('________________________',i,'________________________')
            else:
                # 电子书
                print('——————————————【电子书信息插入】——————————————')
                # 包装
                Package_s = nor_book
                # ISBN
                ISBN_s = '-'
                # 电子书图书名字
                Bookname_s = AA.getEbookname(driver)
                # 电子书评星
                Star_s = AA.getEstar(driver)
                # 电子书评论数
                Comment_amount_s = AA.getEBookComment_amount(driver)
                # 电子书价格
                Bookprice_s = AA.getEBookPrize(driver)

                # 插表
                # print(Bookurl_type_s, Bookname_s, Bookprice_s, nowtime,
                #       Comment_amount_s, Star_s, ISBN_s, Package_s, BookType_s, i)
                opm.addMessageDB(Bookurl_type_s,Bookname_s,Bookprice_s,nowtime,
                                     Comment_amount_s,Star_s,ISBN_s,Package_s,BookType_s,i)

                print('________________________', i, '________________________')

        # 点击TOP图书名 进入详情 窗口切换
        def ClickBooktitle(element,i,Bookprice_s,opm):
            try:
                element.click()
                sleep(1)
                driver.switch_to_window(driver.window_handles[1])  # 切换到详情窗口
                sleep(1)
                AA.alertClose(driver) # 过滤广告弹框 并关闭
                sleep(1)
                # 详情爬取+插入库操作
                InToDetails(i,Bookprice_s,opm)
            except Exception as e:
                Log.logInfo('进入详情 窗口切换',e)
            finally:
                driver.close()
                driver.switch_to_window(driver.window_handles[0])  # 切回到列表窗口

        # 二: 销量榜列表
        TopList = AA.ToplistName(driver) # 书名（元素）
        B_prize = AA.ToplistPrize(driver) # 书价（元素）

        try:
            opm = OPMysql.OPMysql() # 链接数据库
            # 遍历榜单
            for i,Booklist_name in enumerate(TopList[0:10]):
                Log.logInfo(Booklist_name.text)  # 打印书名
                Bookprice_s = B_prize[i].text.replace('￥','')
                ClickBooktitle(Booklist_name,i+1,Bookprice_s,opm)   #点击书名
        except Exception as e:
            Log.logInfo(e)
        finally:
            opm.dispose()  # 关闭数据库连接


# 选择图书分类
def choose_bookType():


    # 初始化对象
    AA = AmazonBM.AmazonMg
    drlist = driverStart() # 取出驱动器数组
    driver = drlist[0] # 得到driver

    type_arr = ['文学','小说','传记','动漫与绘本','少儿','人文社科','哲学',
                '政治与军事','心理学','历史','国学','经济管理','科技','科学与自然',
                '计算机与互联网','旅游与地图','烹饪美食与酒','婚恋与两性','体育']
    # type_arr =['人文社科']

    try:
        Log.logInfo('—————————————— 图书 ——————————————')
        GetAllMessage(driver) # 第一次默认 综合图书抓取
        # 轮循分类
        for i,booktype_str in enumerate(type_arr):
            mark = '{0}{1}{2}'.format('——————————————',booktype_str,'——————————————')
            Log.logInfo(mark)
            try:
                AA.BookTypeClick(driver,booktype_str) # 点击分类 展开Top列表
                GetAllMessage(driver) # 获取详情
            except Exception as E:
                mes = "分类操作失败 -",booktype_str,"\n",E
                Log.logError(mes)
            AA.BackBome(driver) #返回总目录
            sleep(3)
    finally:
        driver.close()  # 关闭浏览器

        if (Server_mode ==True):
            display = drlist[1] # 得到display
            driver.quit()
            display.stop()


if __name__ == '__main__':
    choose_bookType()


