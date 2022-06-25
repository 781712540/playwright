# -*- coding: utf-8 -*-
# @Time    : 2022/6/24 20:37
# @Author  : zhagnyunlong
# @File    : record01.py
import allure
from playwright.sync_api import Playwright, sync_playwright, expect

import yaml
import pytest

with open(file='testcases.yaml', mode='r', encoding='utf-8') as f:
    cases_dict = yaml.safe_load(f)
    # print(cases_dict)

@allure.feature('Playwirght BDD Framework Demo')
class TestWeb:

    def run_step(self, func, value):
        """
        处理每一步执行了什么关键字，及具体的参数
        :param func:
        :param value:
        :return:
        """
        func(*value)

    def run_case(self, case):
        """
        获取所有测试用例
        :param case:
        :return:
        """

        allure.dynamic.title(case['title'])
        allure.dynamic.description(case['des'])

        steps = case['steps']
        try:
            for step in steps:
                func = self.page.__getattribute__(step['method'])
                print(step['name'])
                args = list(step.values())[2:]
                print(args)
                with allure.step(step['name']):
                    self.run_step(func, args)
        except Exception:
            allure.attach(self.page.screenshot(), '用例执行报错截图', allure.attachment_type.PNG)
            pytest.fail('用例执行失败')
        allure.attach(self.page.screenshot(), '用例执行成功截图', allure.attachment_type.PNG)

    def setup_class(self,):
        self.playwirght = sync_playwright().start()
        self.browser = self.playwirght.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    @allure.story('登录')
    @pytest.mark.parametrize('POCcases', cases_dict['baidupage'])
    def test_search(self, POCcases):

        self.run_case(POCcases)
        self.page.wait_for_timeout(3*1000)

    def teardown_class(self):
        self.browser.close()
        self.playwirght.stop()


# #
# if __name__ == '__main__':
#     pytest.main(["-q", "-s", "demo01.py"])