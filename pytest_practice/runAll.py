# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/31 0031 19:22
@Auth ： wanghao
@File ：runAll.py
"""
import os
import sys
import time

BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)
# 测试报告数据
TEST_REPORT = os.path.join(BASE_DIR, "report")
# 测试报告路径
TESTCASES_DIR = os.path.join(BASE_DIR, "report/html")


if __name__ == "__main__":
    print('开始生成测试报告'.center(45, '*'))
    os.system('pytest ' + '--alluredir=' + TEST_REPORT)
    time.sleep(3)
    os.system('allure generate --clean '+ TEST_REPORT + ' -o '+ TESTCASES_DIR)
    print('测试报告生成完毕'.center(45, '*'))