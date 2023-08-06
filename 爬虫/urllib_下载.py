import  urllib.request

#下载网页
url = 'http://www.baidu.com'

#第二个变量是保存的文件名
urllib.request.urlretrieve(url, 'baidu.html')

#下载图片 找到图片,右键->复制图片链接
url_img = 'https://img1.baidu.com/it/u=1960110688,1786190632&fm=253&fmt=auto&app=138&f=JPEG'
#第二个变量是保存的文件名
urllib.request.urlretrieve(url_img, 'baidu.jpg')

#下载视频
# 找到视频,右键->复制图片链接
url_video = 'https://vd3.bdstatic.com/mda-pgfjwrphrs9qdmzm/sc/cae_h264/1689617677064359562/mda-pgfjwrphrs9qdmzm.mp4?v_from_s=hkapp-haokan-hbf&auth_key=1691322158-0-0-59567d1e6168315e5f87a13f1ad39da4&bcevod_channel=searchbox_feed&cr=2&cd=0&pd=1&pt=3&logid=2558775876&vid=638714064640370491&abtest=111803_1&klogid=2558775876'
#第二个变量是保存的文件名
urllib.request.urlretrieve(url_video, 'baidu.mp4')