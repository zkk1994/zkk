'''
Cookie:
http协议：无状态、无连接、媒体独立。
每个请求都是独立的，有一些接口登录后才能访问，需要使用Cookie验证用户是否登录
account/dashboard 用户没有登录时，返回登录的页面
account/dashboard 如果登录了，返回用户的详细信息
如果cookie失效或者换其他用户登录，就不能继续访问了
'''
import requests
# 百格网站，有一些接口登录之后才能访问
url = "https://www.bagevent.com/account/dashboard"
r = requests.get(url)
print(r.text)

# 用Fiddler抓到的包，将里面的头设置到这里
head = {
    "Cookie": '__auc=1dcba38b17627515a12079d882a; _ga=GA1.2.1764775160.1606977415; _gid=GA1.2.1038453811.1606977415; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38; JSESSIONID=F771E5018942255B6B179A28C3FCF028; BAGSESSIONID=86d7baa0-b895-4eb8-b378-a126bdc226a7; __asc=6ffa48d91762cbd2d3dbb3346d0; _gat=1; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1606977411,1606977586,1607068364; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1607068364'
}
print("登录后，返回的结果为：")
r = requests.get(url, headers=head)
print(r.text)