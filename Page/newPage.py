from Base.base import Base
from Page.pageElements import PageElements


class NewPage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def send_phone(self, phone):
        """
        输入手机号
        :param phone: 手机号码
        :return:
        """
        self.send_ele(PageElements.new_sms_recv_phone_id, phone)

    def send_sms(self, sms_data):
        """
        发送短信
        :param sms_data: 发送短信内容
        :return:
        """
        # 输入短信
        self.send_ele(PageElements.new_sms_send_text_id, sms_data)
        # 点击发送按钮
        self.click_ele(PageElements.new_sms_send_btn_id)

    def get_sms_result(self):
        """获取已发送短信内容"""
        # 定位所有内容
        result = self.search_eles(PageElements.new_sms_results_ids)
        # 返回文本列表
        return [i.text for i in result]
