import  urllib.request
import  urllib.parse

#https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6
#实际是https://www.baidu.com/s?wd=周杰伦
#我们平时检索的时，需要中文输入时怎么办？

#Unicode编码把所有语言都统一编码到一起。

#url = 'https://www.baidu.com/s?wd=%E5%91%A8%E6%9D%B0%E4%BC%A6'

#UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-12: ordinal not in range(128)
#url = 'https://www.baidu.com/s?wd=周杰伦'

url = 'https://www.baidu.com/s?wd='

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
}

#将周杰伦名字变成Unicode编码
name = urllib.parse.quote('周杰伦')
print(name)

url_search = url + name
print(url_search)
request = urllib.request.Request(url_search, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)