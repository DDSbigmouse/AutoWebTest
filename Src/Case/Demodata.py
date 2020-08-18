# !/usr/bin/env/python
# -*-coding:utf-8-*-

# import pytest
from functools import wraps
import traceback
from Src.Utils.LoggerIt import get_logger
import os
import sys


def logSome():
    print ("os.path.realpath(__file__)=%s" % os.path.realpath(__file__))


if __name__ == '__main__':
    logSome()
