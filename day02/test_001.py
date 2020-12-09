'''
pytest是一种测试框架，用来方便的组织测试脚本，生成测试报告，或者与其他工具集成、
命名要求：
1.测试文件以test_开头或以_test结尾。
2.测试类以Test开头
3.测试函数方法以test_开头
执行：
1.运行某个文件pytest脚本.py
2.运行某个文件中的某个用例 pytest脚本.py::test_register_001
3.运行生成测试报告：pytest 脚本.py  --html=report.html
3.多线程运行：pytest 脚本.py -n 3
4.失败重执行：pytest 脚本.py -reruns=3
'''
import requests
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
def test_register_001():
    data = {"mobilephone": "1801234567", "pwd":"123456"}
    r = requests.post(url,data=data)
    assert r.json()['msg'] == "手机号码格式不正确"

def test_register_002():
    data = {"mobilephone": "18012345678", "pwd":"1234"}
    r = requests.post(url,data=data)
    assert r.json()['msg'] == "密码长度必须为6~18"

def test_register_003():
    data = {"mobilephone": "18012345678", "pwd":"12341234567889009876522222"}
    r = requests.post(url,data=data)
    assert r.json()['msg'] == "密码长度必须为6~18"
