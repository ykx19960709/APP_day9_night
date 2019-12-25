import allure, pytest


class Test_003:

    # @allure.step("我是一个测试步骤～")
    # def test_003_1(self):
    #     # 添加步骤描述信息
    #     allure.attach("文件名字", "文件内容，具体步骤描述信息")
    #     assert True
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_003_2(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_003_3(self):
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test_003_4(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_003_5(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_003_6(self):
        assert True
