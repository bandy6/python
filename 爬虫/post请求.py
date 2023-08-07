
import urllib.request

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
}

data = {
    'kw': 'good'
}

#post请求参数必须进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

#post的请求参数 是不会拼接url的后面的，而是需要在请求对象定制的参数中
request = urllib.request.Request(url, data, headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)

import  json

obj = json.loads(content)

print(obj)