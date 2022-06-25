# -*- coding: utf-8 -*-
# @Time    : 2022/6/25 16:21
# @Author  : zhagnyunlong
# @File    : run.py
import os

import pytest

if __name__ == '__main__':
    os.system('rd /s/q temp')
    os.system('rd /s/q report')
    pytest.main(['-s', 'demo01.py', '--alluredir', './temp'])
    os.system('allure generate ./temp -o ./report --clean')
