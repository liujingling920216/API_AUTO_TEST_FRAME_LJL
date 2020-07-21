import json
import re


acture_value = {"tags": [{"id": 2,"name": "星标组","count": 0},{"id": 133,"name": "广东","count": 0},{"id": 136,"name": "广西","count": 4},{"id": 137,"name": "广东1","count": 0},{"id": 138,"name": "石湾03","count": 0}]}

str(acture_value["tags"][2])
print(type(acture_value["tags"][2]))

expect_value = '{"id":(.+?),"name":"(.+?)","count":(.+?)}'
value = re.findall(expect_value,acture_value["tags"][2])
if value:
    print(True)
else:
    print(False)
