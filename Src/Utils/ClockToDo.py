



import platform
import time
import datetime
import os,sys

# # 取当前的时间1
# now=datetime.datetime.now()
# print('now =',now)
# demo 当前时间2
# def pr():
#     nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     print ('DDS ',nowtime)

# # target时间
# sched_Timer=datetime.datetime(2017,12,12,15,31,00)#年-月-日-时-分-秒
# print('sched_Timer =',sched_Timer)

#测试用方法
def doSth():
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    print('test-dododo',now)
    # 假装做这件事情需要一分钟



# 定时方法 目标时间 间隔 方法
def timeFun(sched_Timer,intvalue,ds):#type=hours/minutes/seconds
    flag=0
    while True:  #判断逻辑  如果现在时间=target时间
        now=datetime.datetime.now()
        if (now.hour == sched_Timer.hour)and(now.minute == sched_Timer.minute)and(now.second == sched_Timer.second)and(flag==0):
            ds()
            flag=1
            time.sleep(1)
        else:           #判断逻辑  如果现在时间 ?= target时间
            if flag==1:
                sched_Timer = sched_Timer+datetime.timedelta(hours=intvalue)
                flag=0



if __name__ == '__main__':
    now = datetime.datetime.now()
    sched_2h = now + datetime.timedelta(seconds=3)
    #调用定时任务
    timeFun(sched_2h,10,doSth)# 执行一次

















