'''
fixture作用域：session级别
公共方法放到conftest.py文件中，文件名字不能写错，pytest是根据文件名字找到所以对用的方法的。
1.conftest文件可以存在多个
2.conftest放在SessionTest目录下，对SessionTest下的py文件及子目录下的py文件生效。
3.conftest放在ApiAuto目录下，对整个工程生效
4.不用import
'''

import pytest

# session级别的，整个执行过程，开始前执行前置，所有执行完了之后执行后置
@pytest.fixture(scope='session')
def login():
    print("登录系统")
    yield
    print("退出系统")