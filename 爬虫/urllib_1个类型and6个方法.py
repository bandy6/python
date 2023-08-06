import  urllib.request

url = 'http://www.baidu.com'

#模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

#一个类型和六个方法
#response 是一个HTTPResponse的类型
#print(response)

#按照一个字节一个字节都
#content =response.read()
#print(content)

#读取前5字节
#content = response.read(5)
#print(content)

#按行读
#content = response.readline()
#print(content)

#读多行
#content = response.readlines()
#print(content)

#获取状态码200 OK
#print(response.getcode())



#获取状态码200 OK
print(response.geturl())
