# -*- coding: utf-8 -*-

import logging
import os
import sys
from utils import EmailSend
from time import sleep



# 获取logger实例，如果参数为空则返回root logger
logger = logging.getLogger("AppName")

# 指定logger输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')



if not logger.handlers:
    # 创建文件日志
    file_handler = logging.FileHandler('TextLog.txt')
    file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

    # 控制台日志
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.formatter = formatter  # 也可以直接给formatter赋值

    # 为logger添加的日志处理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # 指定日志的最低输出级别，默认为WARN级别
    logger.setLevel(logging.INFO)

    # 移除一些日志处理器 ！！！避免重复打印！！！ 重要！！！
    # logger.removeHandler(file_handler)


# Error
def logError(*args):
    str = '{0}'.format(*args)
    logger.error('Error message:%s' % str)
    EmailSend.SendEmialNoitce('Error message:%s' % str)

# information
def logInfo(*args):
    str = '{0}'.format(*args)
    logger.info('Info message: %s' % str)


