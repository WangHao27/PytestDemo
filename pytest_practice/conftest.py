# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/31 0031 17:57
@Auth ： wanghao
@File ：conftest.py
"""
import os
import pytest
import yaml
from pytest_practice.common.calc import Calculator

with open(f"{os.path.dirname(__file__)}/datas/calc.yaml") as f:
    data = yaml.safe_load(f)
    #获取add数据
    add_datas = data['add']['datas']
    #获取div数据
    div_datas = data['div']['datas']
    #获取sub数据
    sub_datas = data['sub']['datas']
    # 获取mul数据
    mul_datas = data['mul']['datas']

@pytest.fixture(scope="module")
def get_calc():
    print("实例化计算器类")
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")

@pytest.fixture(params=add_datas, ids=data['add']['myid'])
def get_add_datas(request):
    # 获取加法数据并返回
    datas = request.param
    yield datas


@pytest.fixture(params=div_datas, ids=data['div']['myid'])
def get_div_datas(request):
    # 获取除法数据并返回
    datas = request.param
    yield datas



@pytest.fixture(params=sub_datas, ids=data['sub']['myid'])
def get_sub_datas(request):
    # 获取减法数据并返回
    datas = request.param
    yield datas


@pytest.fixture(params=mul_datas, ids=data['mul']['myid'])
def get_mul_datas(request):
    # 获取乘法数据并返回
    datas = request.param
    yield datas
