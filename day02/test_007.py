'''
fixture带参数
'''
import pytest
import requests

# 测试数据
# 参数使用params关键字，一个列表，列表中有5组数据，前3组数据是字典
# @pytest.fixture(params=[{"username": "root", "pwd": "123456"},
#                         {"username": "admin", "pwd": "888888"},
#                         {"username": "adminstractor", "pwd": "HelloPwd"},
#                         "four",
#                         5])
# def login_data(request): # 参数request是固定的，不能写其他的
#     return request.param # 使用request.param返回每组数据
#
# # 测试逻辑（测试步骤）
# # 登录功能的测试脚本
# def test_login(login_data):
#     print(f"测试登录功能，测试数据为：{login_data}")

# 练习： 注册接口的测试代码，用这种方式来实现。
@pytest.fixture(params=[
    {"data":{"mobilephone":"13384563820", "pwd": "123456","name": None }, "expect":{"msg":"注册成功","code":"10001"}},
    {"data":{"mobilephone":"13394563811", "pwd": "123456789012345678","name": None }, "expect":{"msg":"注册成功","code":"10001"}},
    {"data":{"mobilephone":"13304561134", "pwd": "13245","name": "翔翔"}, "expect":{"msg":"密码长度必须为6~18","code":"20108"}}
    ])

def register_data(request):
    return request.param

def test_register(register_data):
    url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
    print("测试数据",register_data['data'])
    print("测试结果",register_data['expect'])
    r = requests.post(url, data=register_data['data'])
    print(r.text)
    assert r.json()['msg'] == register_data['expect']['msg']
    assert r.json()['code'] == register_data['expect']['code']