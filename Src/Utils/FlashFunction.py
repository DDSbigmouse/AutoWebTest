# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 公共函数
import logging
from Src.Utils.LoggerIt import get_logger
import traceback
import os


# log装饰器-元素定位
def logDec(func):
    # @wraps(func)
    def log(*args, **kwargs):
        # noinspection PyBroadException
        try:
            print("当前运行方法", func.__name__)
            return func(*args, **kwargs)
        except Exception as e:
            print("————logging————")
            # get_logger().error(f"{func.__name__} is error,here are details:{traceback.format_exc()}")
            get_logger().error(f"'当前路径 =' {os.getcwd()} \n"
                               f"定位 {func.__name__} is error,here are details: {'元素未找到'}")

    return log


# log装饰器-断言
def logAlert(func):
    # @wraps(func)
    def log(*args, **kwargs):
        # noinspection PyBroadException
        try:
            print("当前运行方法", func.__name__)
            return func(*args, **kwargs)
        except AssertionError as e:
            print("————logging————")
            print("当前路径 =", os.path.realpath(__file__))
            get_logger().error(f"'当前路径 =' {os.getcwd()} \n"
                               f"断言 {func.__name__} is error,here are details: {e}")

    return log
