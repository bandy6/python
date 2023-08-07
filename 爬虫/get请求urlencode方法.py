import urllib.request
import urllib.parse
#https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
#实际是https://www.baidu.com/s?wd=周杰伦&location=中国台湾省


url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
}

data = {
    'wd': '周杰伦',
    'location': '中国台湾省'
}


#将周杰伦名字变成Unicode编码
data = urllib.parse.urlencode(data)

url_search = url + data
print(url_search)
request = urllib.request.Request(url_search, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)