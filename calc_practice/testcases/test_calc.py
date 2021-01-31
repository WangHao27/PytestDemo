# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/30 0030 21:30
@Auth ： wanghao
@File ：test_calc.py
"""
import pytest
import yaml
from calc_practice.common.calc import Calculator


with open("../datas/calc.yaml") as f:
    data = yaml.safe_load(f)
    #获取add数据
    add_datas = data['add']['datas']
    #获取div数据
    div_datas = data['div']['datas']
    myid = data['add']['myid']

class TestCalcutor:
    #所有用例开始前执行
    def setup_class(self):
        self.calc = Calculator()
        print("计算开始")

    #所有用例执行完后执行
    def teardown_class(self):
        print("用例执行结束")

    @pytest.mark.parametrize("a,b,expect", add_datas, ids=myid)
    def test_add(self, a, b, expect):
        #调用加法
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", div_datas)
    def test_div(self, a, b, expect):

        if b == 0:
            print("被除数不能为零")
            assert False
        #调用除法
        result = self.calc.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect


