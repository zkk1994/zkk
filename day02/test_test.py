# 练习： 注册接口的测试代码，用这种方式来实现。

import pytest
@pytest.fixture(params=[
    {"data":{"mobilephone":"13324563840", "pwd": "123456","name": None }, "except":{"msg":"注册成功","code":10001}},
    {"data":{"mobilephone":"13324563841", "pwd": "123456789012345678","name": None }, "except":{"msg":"注册成功","code":10001}},
    {"data":{"mobilephone":"13324561234", "pwd": "133245","name": "翔翔"}, "except":{"msg":"密码长度为6~18位","code":10002}}
    ])

def register_data(request):
    return request.param

def test_register(register_data):
    print("测试数据",register_data['data'])
    print("测试结果",register_data['except'])