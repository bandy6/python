import  urllib.request

url = 'https://www.baidu.com'


#https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
#url的组成
#协议            主机         端口号    路径         参数           锚点
#http/https  www.baidu.com    80       s          ?后面数据
#端口：http 80 https 443 mysql 3306

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
}

#因为urlopen方法不能直接传入字典
#请求对象的定制
request = urllib.request.Request(url, headers = headers)

#response = urllib.request.urlopen(url)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

print(content)
#打印内容不全，因为遇到了UA反爬
#查找User-Agent:网页右键->检查，选择网络(network),刷新页面。此时选择header,拉取到最下方