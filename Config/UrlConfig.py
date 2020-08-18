# coding='utf-8


class Server:
    Server_mode = False  # 服务器模式 需要置True


UrlModel = "uat"  # 测试
# UrlModel = "www"  # 生产


class TestUrl:
    nakedRetreats = "https://" + UrlModel + ".nakedretreats.cn/zh-CN/"  # 裸心官网主站
    nakedStable = "https://" + UrlModel + ".nakedretreats.cn/naked-stables/zh-CN/"  # 裸心谷官网
    nakedCastle = "https://" + UrlModel + ".nakedretreats.cn/naked-castle/zh-CN/"  # 裸心堡官网
