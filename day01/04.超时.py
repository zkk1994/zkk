'''
超时：
1.上传的文件比较大，比如2G的文件，默认的时间内上传不完，可以设置大一点的超时时间
2.接口有性能要求，比如接口必须在0.5秒内返回，可以设置超时时间为0.5
'''

import requests
# 获取用户列表的接口
for i in range(10):
    try:
        url = "http://192.168.150.54:8089/futureloan/mvc/api/member/list"
        r = requests.get(url, timeout=0.5)
        print(r.text)
    except Exception as e:
        print(e)