import  urllib.request
import urllib.parse


url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

#此时会打印未知错误
#headers = {
#    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
#}

headers = {
    'Cookie':
'ZFY=4rsXc93Hd7nxqsle1ThEtVEBIxPo5Jj2S6UPbU2XQoA:C; BIDUPSID=E43475FD8B10DABF91829C47D5002E97; PSTM=1691368867; BAIDUID=E43475FD8B10DABF3FA19A71F77857CA:FG=1; BAIDUID_BFESS=E43475FD8B10DABF3FA19A71F77857CA:FG=1; BA_HECTOR=200l8l8k0k8k85al8ga52k0o1id0fd21o; PSINO=1; delPer=0; H_PS_PSSID=36560_39112_38831_38878_39114_38917_26350_39132_39100_39043; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1691368873; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1691368946; ab_sr=1.0.1_YjIxYmIxNGM4NzhhOTgxNTJmMjVhYjIzZDY1MDZlZDA5MTAyYjAzYzRiNDIwMDE1MmI4YzRiZmZhMGJmNDQ1YWQ5NzU2MjE1Y2U0OTA1MTJjZGY2N2ZkZGJmYzk2NTExNWY4ZDVkMTQzOTgxNGQ5YjFlODFlZGVjZmM2YjJhMGYzMjJkOGE0OTdhNDY5NDU3NThjYmQ5ZGZhYTg0OWVmZQ=='

}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'good',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '262931.57378',
    'token': '96ca4383fb306c77aeffdd6041a9d6a6',
    'domain': 'common',
    'ts': '1691369270189',
}

data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url, data, headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

#print(content)

import json

obj = json.loads(content)
print(obj)