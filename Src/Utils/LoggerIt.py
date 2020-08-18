# -*- coding: utf-8 -*-
import os
import time
import logging
import sys

"""
    logging 日志级别

    DEBUG	     最详细的日志信息，典型应用场景是 问题诊断
    INFO	     信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那样进行工作
    WARNING	     当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正常运行的
    ERROR	     由于一个更严重的问题导致某些功能不能正常运行时记录的信息
    CRITICAL	 当发生严重错误，导致应用程序不能继续运行时记录的信息
"""

# 创建日志打印路径
log_dir1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
# 日志打印时间
today = time.strftime('%Y%m%d', time.localtime(time.time()))
# 日志格式 路径+时间点
full_path = os.path.join(log_dir1, today)
# 创建日志文件，如果不存在重名则创建
if not os.path.exists(full_path):
    os.makedirs(full_path)
log_path = os.path.join(full_path, "LoggerError.log")


def get_logger():
    # 获取logger实例，如果参数为空则返回root logger
    logger = logging.getLogger("LoggerError")
    if not logger.handlers:
        # 指定logger输出格式
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

        # 文件日志
        file_handler = logging.FileHandler(log_path, encoding="utf8")
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
    return logger