# -*- coding:utf-8 -*
# 测试用例 — 用来测试官网主站
from Src.Case.Element import RetreatsElement
from Src.Utils.FlashFunction import logAlert
import pytest

NR = RetreatsElement.Retreats()  # 创建元素类的对象


class TestRetreats:

    # 启动驱动
    @staticmethod
    def setup_class():
        NR.driverStart()

    # 验证界面有 "裸心谷"
    @logAlert
    def test_tabStables(self):
        str_tab = NR.tabStablesElement().text
        assert str_tab == "裸心谷"

    # 验证界面有 "裸心堡"
    @logAlert
    def test_tabCastle(self):
        str_tab = NR.tabCastleElement().text
        assert str_tab == "裸心堡"

    # 验证界面有 "裸心帆"
    @logAlert
    def test_tabSail(self):
        str_tab = NR.tabSailElement().text
        assert str_tab == "裸心帆"

    # 验证界面有 "即将开业"
    @logAlert
    def test_tabOther(self):
        str_tab = NR.tabOtherElement().text
        assert str_tab == "即将开业酒店"

    # 验证界面有 "团队建设"
    @logAlert
    def test_tabTeambuilding(self):
        str_tab = NR.tabTeambuildingElement().text
        assert str_tab == "团队建设"

    # 验证界面有 "关于裸心度假村"
    @logAlert
    def test_about(self):
        str_about = NR.aboutElement().text
        assert str_about == "关于裸心度假村"

    # 验证界面顶部有 "预定按钮"
    @logAlert
    def test_topBookBtn(self):
        str_about = NR.topBookButtonElement().text
        assert str_about == "预订房间"

    # 验证界面顶部有 "中英按钮"
    @logAlert
    def test_enFontBtn(self):
        str_about = NR.enFontBtnElement().text
        assert str_about == "EN"

    # 验证界面顶部有 "查找客房按钮"
    @logAlert
    def test_FindRoomBtn(self):
        str_about = NR.findRoomBtnElement().text
        assert str_about == "查找客房"

    # 验证界面 含有"优惠套餐" title
    @logAlert
    def test_FindRoomBtn(self):
        str_about = NR.specialOfferElement().text
        assert str_about == "优惠套餐"

    # 验证界面 含有"裸心度假村" title
    @logAlert
    def test_allHotel(self):
        str_about = NR.allHotelsElement().text
        assert str_about == "裸心度假村"

    # 即将开业酒店 title
    @logAlert
    def test_AllOtherHotel(self):
        str_about = NR.fluidAllOtherElement().text
        assert str_about == "即将开业酒店1"

    # 测试类级结束
    @staticmethod
    def teardown_class():
        NR.driverClose()


if __name__ == '__main__':
    pytest.main()
