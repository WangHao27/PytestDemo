# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/31 0031 18:39
@Auth ： wanghao
@File ：test_calc.py
"""
import allure
import pytest


@allure.feature("计算器测试")
class TestCalcutor:

    @allure.story("测试加法")
    @pytest.mark.run(order=2)  #pytest-ordering插件,自定义排序为最先执行
    def test_add(self, get_calc, get_add_datas):
        # 步骤说明
        with allure.step("计算两个数的和"):
            result = get_calc.add(get_add_datas[0],get_add_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_add_datas[2]

    @allure.story("测试除法")
    @pytest.mark.run(order=7)
    def test_div(self, get_calc, get_div_datas):
        # 步骤说明
        with allure.step("计算两个数相除"):
            result = get_calc.div(get_div_datas[0], get_div_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_div_datas[2]

    @allure.story("测试减法")
    @pytest.mark.run(order=3)
    def test_sub(self, get_calc, get_sub_datas):
        # 步骤说明
        with allure.step("计算两个数的差"):
            result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_sub_datas[2]

    @allure.story("测试乘法")
    @pytest.mark.run(order=5)
    def test_mul(self, get_calc, get_mul_datas):
        # 步骤说明
        with allure.step("计算两个数的乘积"):
            result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_mul_datas[2]
