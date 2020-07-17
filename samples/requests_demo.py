import requests

req_get = requests.get(url='https://api.weixin.qq.com/cgi-bin/token',params={'secret': '65515b46dd758dfdb09420bb7db2c67f', 'appid': 'wx55614004f367f8ca', 'grant_type': 'client_credential'})
print(type(req_get))