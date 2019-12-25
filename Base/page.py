from Page.homePage import HomePage
from Page.newPage import NewPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    def get_home_page(self):
        """返回短信首页实例化"""
        return HomePage(self.driver)

    def get_new_page(self):
        """返回新建页面对象"""
        return NewPage(self.driver)
