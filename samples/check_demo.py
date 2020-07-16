import re
import ast

# 1.正则匹配
# 实际结果
acture01 = '{"access_token":"35_BKh82IAvv_7Obcdwyre-v60qGrcS5rrWo-XN24oxrKZ4Xxh8OIcsa3FahcUsrB_6hY5zEXpx7adPDHNLkFGQuqJY80BHsZc8fIXXkXiMTlvA-hZe5o_KJRlyyVnAXWsywtW5k9vw_1lZ-1IiINAdACAMRE","expires_in":7200}'
# 预期结果
expect01 = '{"access_token":"(.+?)","expires_in":(.+?)}'

value = re.findall(expect01,acture01)
# print(value)
if value:
    print(True)
else:
    print(False)

# 2.json键匹配
expect02 = 'access_token,expires_in'
acture02 = '{"access_token":"35_BKh82IAvv_7Obcdwyre-v60qGrcS5rrWo-XN24oxrKZ4Xxh8OIcsa3FahcUsrB_6hY5zEXpx7adPDHNLkFGQuqJY80BHsZc8fIXXkXiMTlvA-hZe5o_KJRlyyVnAXWsywtW5k9vw_1lZ-1IiINAdACAMRE","expires_in":7200}'
acture_dict02=ast.literal_eval(acture02)     #结果：dict_keys(['expires_in', 'access_token'])
# print(acture_dict02.keys())
expect_key = expect02.split(',')     #结果：['access_token', 'expires_in']
# print(expect_key)
for key in expect_key:
    result = True
    if key in acture_dict02:
        result = True
    else:
        result = False
    if not result:
        break
print(result)

# json键值对匹配
expect03 = '{"errcode":0,"errmsg":"ok"}'
acture03 = {"errcode":0,"errmsg":"ok"}
expect_dict03 = ast.literal_eval(expect03)

for v in acture03.items():
    result = True
    if v in expect_dict03.items():
        result =  True
    else:
        result = False
    if not result:
        break
print(result)








