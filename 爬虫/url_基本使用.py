import urllib.request

#定义一个url,就是要访问的地址
url = 'http://www.baidu.com'

#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

#获取网页内容
content = response.read().decode('utf-8')

#打印信息
print(content)