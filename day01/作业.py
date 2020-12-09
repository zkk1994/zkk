import requests
# 注册
# sign_001
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
# user = {
#     "mobilephone":"13324563840",
#     "pwd":"123456",
#     "name": None
# }
# r = requests.post(url, data=user)
# print(r.json())
# r = r.json()
# assert r["msg"]=='注册成功'
#
# # sign_002
# user = {
#     "mobilephone":"13324563841",
#     "pwd":"123456789012345678",
#     "name": None
# }
# r = requests.post(url, data=user)
# print(r.json())
# r = r.json()
# assert r["msg"]=='注册成功'

# sign_003
# user = {
#     "mobilephone":"13324563842",
#     "pwd":"123456",
#     "name": "瑶瑶"
# }
# r = requests.post(url, data=user)
# print(r.json())
# r = r.json()
# assert r["msg"]=='注册成功'

# sign_004
# user = {
#     "mobilephone":"13324563843",
#     "pwd":"123456",
#     "name": "瑶瑶"
# }
# r = requests.post(url, data=user)
# print(r.json())
# r = r.json()
# assert r["msg"]=='注册成功'

# sign_005
# user = {
#     "mobilephone":"133245638435",
#     "pwd":"123456",
#     "name": None
# }
# r = requests.post(url, data=user)
# print(r.json())
# r = r.json()
# assert r["msg"]=='手机号码格式不正确'

# sign_006
# user = {
#     "mobilephone":None,
#     "pwd":"123456",
#     "name":"瑶瑶"
# }
# r = requests.post(url, data=user)
# print(r.json())
# r = r.json()
# assert r["msg"]=='手机号不能为空'

# sign_007
# user = {
#     "mobilephone":1332456384,
#     "pwd":"123456",
#     "name":None
# }
# r = requests.post(url, data=user)
# print(r.json())
# r = r.json()
# assert r["msg"]=='手机号码格式不正确'

# sign_008
# user = {
#     "mobilephone":1332456385,
#     "pwd":"123456",
#     "name":"大禹"
# }
# r = requests.post(url, data=user)
# print(r.json())
# r = r.json()
# assert r["msg"]=='手机号码格式不正确'

# sign_009
# user = {
#     "mobilephone":133245638578,
#     "pwd":"123456",
#     "name":None
# }
# r = requests.post(url, data=user)
# print(r.json())
# r = r.json()
# assert r["msg"]=='手机号码格式不正确'

# sign_010
# user = {
#     "mobilephone":1332456385789,
#     "pwd":"123456",
#     "name":"大禹"
# }
# r = requests.post(url, data=user)
# print(r.json())
# r = r.json()
# assert r["msg"]=='手机号码格式不正确'

# sign_011
# user = {
#     "mobilephone":"13333da",
#     "pwd":"123456",
#     "name":None
# }
# r = requests.post(url, data=user)
# print(r.json())
# r = r.json()
# assert r["msg"]=='手机号码格式不正确'

# sign_012
# user = {
#     "mobilephone":"13333！",
#     "pwd":"123456",
#     "name":"阿干"
# }
# r = requests.post(url, data=user)
# print(r.json())
# r = r.json()
# assert r["msg"]=='手机号码格式不正确'

# sign_013
# user = {
#     "mobilephone":"122222334大",
#     "pwd":"123456",
#     "name":None
# }
# r = requests.get(url,params=user)
# print(r.json())
# r = r.json()
# assert r['msg'] == '手机号码格式不正确'

# sign_014
# user = {
#     "mobilephone":"122222334大大",
#     "pwd":"123456",
#     "name":"瑶瑶"
# }
# r = requests.get(url,params=user)
# print(r.json())
# r = r.json()
# assert r['msg'] == '手机号码格式不正确'

# sign_015
# user = {
#     "mobilephone":"12046572378",
#     "pwd":"123456",
#     "name":"琪琪"
# }
# r = requests.get(url,params=user)
# print(r.json())
# r = r.json()
# assert r['msg'] == '手机号码格式不正确'

# sign_016
# user = {
#     "mobilephone":"12546572345",
#     "pwd":"123456",
#     "name":None
# }
# r = requests.get(url,params=user)
# print(r.json())
# r = r.json()
# assert r['msg'] == '手机号码格式不正确'

# sign_017
# user = {
#     "mobilephone":"13324561234",
#     "pwd":"12345",
#     "name":"翔翔"
# }
# r = requests.get(url,params=user)
# print(r.json())
# r = r.json()
# assert r['msg'] == '密码长度必须为6~18'

# sign_018
# user = {
#     "mobilephone":"13324561235",
#     "pwd":"12345",
#     "name":None
# }
# r = requests.get(url,params=user)
# print(r.json())
# r = r.json()
# assert r['msg'] == '密码长度必须为6~18'

# sign_019
# user = {
#     "mobilephone":"13324561236",
#     "pwd":"12342222222222225",
#     "name":None
# }
# r = requests.get(url,params=user)
# print(r.json())
# r = r.json()
# assert r['msg'] == '密码长度必须为6~18'

# sign_020
# user = {
#     "mobilephone":"13324561236",
#     "pwd":"12342222222222225",
#     "name":"蛐蛐"
# }
# r = requests.get(url,params=user)
# print(r.json())
# r = r.json()
# assert r['msg'] == '密码长度必须为6~18'

# sign_021
# user = {
#     "mobilephone":"13324561236",
#     "pwd":None,
#     "name":"太阳花"
# }
# r = requests.get(url,params=user)
# print(r.json())
# r = r.json()
# assert r['msg'] == '密码不能为空'

# sign_022
# user = {
#     "mobilephone":"13324561236",
#     "pwd":None,
#     "name":None
# }
# r = requests.get(url,params=user)
# print(r.json())
# r = r.json()
# assert r['msg'] == '密码不能为空'

# sign_023
# user = {
#     "mobilephone":"13324563842",
#     "pwd":"1234565",
#     "name":None
# }
# r = requests.get(url,params=user)
# print(r.json())
# r = r.json()
# assert r['msg'] == '手机号码已被注册'

# sign_024
# user = {
#     "mobilephone":"13324563842",
#     "pwd":"1234565",
#     "regname":"花花"
# }
# r = requests.get(url,params=user)
# print(r.json())
# r = r.json()
# assert r['msg'] == '手机号码已被注册'


# 登录
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
# login_01
user = {
    "mobilephone":"13324563840",
    "pwd":"123456"
}
r = requests.post(url, data=user)
print(r.json())
r = r.json()
assert r["msg"]=='登录成功'

# login_02
user = {
    "mobilephone":None,
    "pwd":"123456789012345678"
}
r = requests.post(url, data=user)
print(r.json())
r = r.json()
assert r["msg"]=='手机号不能为空'

# login_03
user = {
    "mobilephone":"13324563",
    "pwd":"123456"
}
r = requests.post(url, data=user)
print(r.json())
r = r.json()
assert r["msg"]=='用户名或密码错误'

# login_04
user = {
    "mobilephone":"1332456385431",
    "pwd":"123456"
}
r = requests.post(url, data=user)
print(r.json())
r = r.json()
assert r["msg"]=='用户名或密码错误'

# login_05
user = {
    "mobilephone":"13324563765",
    "pwd":"123456"
}
r = requests.post(url, data=user)
print(r.json())
r = r.json()
assert r["msg"]=='用户名或密码错误'

# login_06
user = {
    "mobilephone":"13324563854",
    "pwd":None
}
r = requests.post(url, data=user)
print(r.json())
r = r.json()
assert r["msg"]=='密码不能为空'

# login_07
user = {
    "mobilephone":"13324563854",
    "pwd":"12345"
}
r = requests.post(url, data=user)
print(r.json())
r = r.json()
assert r["msg"]=='用户名或密码错误'

# login_08
user = {
    "mobilephone":"13324563854",
    "pwd":"12345363782829929292878"
}
r = requests.post(url, data=user)
print(r.json())
r = r.json()
assert r["msg"]=='用户名或密码错误'