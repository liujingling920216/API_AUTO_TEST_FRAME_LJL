#coding=utf-8
import json
import re

acture_value = {"tags": [{"id": 2,"name": "星标组","count": 0},
                         {"id": 133,"name": "广东","count": 0},
                         {"id": 136,"name": "广西","count": 4},
                         {"id": 137,"name": "广东1","count": 0},
                         {"id": 138,"name": "石湾03","count": 0}]}
# acture_value=json.dumps((acture_value["tags"][2]),ensure_ascii=False)
acture_value=str(acture_value["tags"][2])

print(acture_value)
expect_value = str({"id":136,"name":"(.+?)","count":4})
print(expect_value)
value = re.findall(expect_value,acture_value)
if value:
    print(True)
else:
    print(False)
