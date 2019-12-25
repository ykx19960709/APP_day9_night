from Base.base import Base
from Page.pageElements import PageElements


class HomePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_new_sms_btn(self):
        """点击新建短信按钮"""
        self.click_ele(PageElements.home_sms_new_btn_id)
