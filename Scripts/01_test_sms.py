import pytest, sys, os

sys.path.append(os.getcwd())

from Base.page import Page
from Base.getDriver import get_android_driver


class TestSms:

    def setup_class(self):
        # 声明driver
        self.driver = get_android_driver("com.android.mms", ".ui.ConversationList")
        # 实例化统一入口类
        self.page = Page(self.driver)


    def teardown_class(self):
        """关闭driver"""
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def goto_new_sms_page(self):
        """进入短信新建页面 -自动运行1次"""
        # 首页点击新建
        self.page.get_home_page().click_new_sms_btn()
        # 新建页面输入手机号码
        self.page.get_new_page().send_phone("13300008888")

    @pytest.mark.parametrize("text", ["hello", "world", "appium"])
    def test_send_sms(self, text):
        """
        发送短信测试方法
        :param text: 发送短信内容
        :return:
        """
        # 发送短信
        self.page.get_new_page().send_sms(text)
        # 断言结果
        assert text in self.page.get_new_page().get_sms_result()
