# coding: utf-8
# ! /usr/bin/env python3

from Config import UrlConfig
from selenium import webdriver
import os
from Src.Utils.FlashFunction import logDec

config_rul = UrlConfig.TestUrl.nakedRetreats  # 配置URL
root_path = os.path.abspath(os.path.dirname(__file__)).split('AutoWebTest')[0]  # 驱动路径


# 驱动
class Retreats(object):
    # print("根目录" + root_path)
    # print("os目录" + os.getcwd())

    # 初始化
    def __init__(self):
        path = 'AutoWebTest/Drivers/chromedriver'
        self.driver = webdriver.Chrome(executable_path=root_path + path)  # 配置驱动路径
        self.url = config_rul  # 配置URL

    # 驱动启动配置
    def driverStart(self):
        # 客户端selenium窗口
        self.driver.get(self.url)
        # 设置隐式等待
        self.driver.implicitly_wait(3)

    # 关闭驱动
    def driverClose(self):
        self.driver.close()  # 关闭浏览器

    # —————————————— 元素定位方法 ——————————————————
    # 裸心谷 tab
    @logDec
    def tabStablesElement(self):
        tab_a = self.driver.find_element_by_css_selector("[class='stables nav-item']")
        return tab_a

    # 裸心堡 tab
    @logDec
    def tabCastleElement(self):
        tab_a = self.driver.find_element_by_css_selector("[class='castle nav-item']")
        return tab_a

    # 裸心帆 tab
    @logDec
    def tabSailElement(self):
        tab_a = self.driver.find_element_by_css_selector("[class='sail nav-item']")
        return tab_a

    # 即将开业酒店 tab
    @logDec
    def tabOtherElement(self):
        tab_a = self.driver.find_element_by_css_selector("[class='other nav-item has-sub']")
        return tab_a

    # 团队建设 tab
    @logDec
    def tabTeambuildingElement(self):
        tab_a = self.driver.find_element_by_css_selector("[class='teambuilding nav-item']")
        return tab_a

    # 关于裸心度假村
    @logDec
    def aboutElement(self):
        about = self.driver.find_element_by_css_selector("[class='container-fluid about-container'] > div > h2")
        return about

    # 右上角预定按钮
    @logDec
    def topBookButtonElement(self):
        btn = self.driver.find_element_by_css_selector("[class='button-primary book-button'] > span")
        return btn

    # 中英切换按钮
    @logDec
    def enFontBtnElement(self):
        btn = self.driver.find_element_by_css_selector("[class='enfont lang']")
        return btn

    # 查找客房按钮
    @logDec
    def findRoomBtnElement(self):
        btn = self.driver.find_element_by_css_selector("[class='form-submit'] > [class='button-primary']")
        return btn

    # 优惠套餐 title
    @logDec
    def specialOfferElement(self):
        btn = self.driver.find_element_by_css_selector("[class='special-offer-container'] > h2")
        return btn

    # 裸心度假村 title
    @logDec
    def allHotelsElement(self):
        btn = self.driver.find_element_by_css_selector("[class='container-fluid all-projects hidden-xs'] > h2")
        return btn

    # 即将开业酒店 title
    @logDec
    def fluidAllOtherElement(self):
        btn = self.driver.find_element_by_css_selector("[class='container-fluid all-other-projects'] > h2")
        return btn











