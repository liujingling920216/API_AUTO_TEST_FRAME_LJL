import re

import jsonpath

acture_value = {"tags": [{"id": 2,"name": "星标组","count": 0},
                         {"id": 133,"name": "广东","count": 0},
                         {"id": 136,"name": "广西","count": 4},
                         {"id": 137,"name": "广东1","count": 0},
                         {"id": 138,"name": "石湾03","count": 0}]}
acture_value=str(acture_value["tags"][2])
print(acture_value)

expect_value = '{"id":136,"name":"(.+?)","count":4}'
value = re.findall(expect_value,acture_value)
if value:
    print(True)
else:
    print(False)
