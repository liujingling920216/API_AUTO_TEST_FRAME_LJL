import ast
import re

class CheckUtils:
    def __init__(self,acture_value=None):
        self.acture_value = acture_value
        self.check_rules = {
            '无': self.no_check,
            'json键是否存在': self.check_key,
            'json键值对': self.check_key_value,
            '正则匹配': self.check_regexp
        }

        self.pass_result = {
            'code':0,
            'response_reason':self.acture_value.reason,
            'response_code':self.acture_value.status_code,
            'response_headers':self.acture_value.headers,
            'response_body':self.acture_value.text,
            'check_result':True,
            'message':''
        }

        self.fail_result =  {
            'code':2,
            'response_reason':self.acture_value.reason,
            'response_code':self.acture_value.status_code,
            'response_headers':self.acture_value.headers,
            'response_body':self.acture_value.text,
            'check_result':False,
            'message':''
        }

    def no_check(self):
        return True

    def check_regexp(self,expect_value=None):
        regexp_value = re.findall(expect_value,self.acture_value.text)
        if regexp_value:
        # pattern = re.compile(expect_value)
        # if re.findall(pattern=pattern,string=self.acture_value):
            return self.pass_result
        else:
            return self.fail_result

    def check_key(self,expect_value=None):
        check_result = []
        wrong_key = []
        expect_value_list = expect_value.split(",")
        result = True
        for key in expect_value_list:
            if key in self.acture_value.keys():
                check_result.append(result)
            else:
                result =  False
                check_result.append(result)
                wrong_key.append(key)
        if False in check_result:
            return self.fail_result
        else:
            return self.pass_result

    def check_key_value(self,expect_value=None):
        check_result = []
        wrong_key_value = []
        expect_dict_value = ast.literal_eval(expect_value)
        for v in self.acture_value.json().items():
            if v in expect_dict_value.items():
                check_result.append(self.pass_result)
            else:
                check_result.append(self.fail_result)
                wrong_key_value.append(v)
            if False in check_result:
                return self.fail_result
            else:
                return self.pass_result

    def run_check(self,check_method,expect_value):
        code = self.acture_value.status_code
        if code == 200:
            if check_method in self.check_rules.keys():
                result = self.check_rules[check_method](expect_value)
                return result
            else:
                self.fail_result['message'] = '不支持%s判断方法'%check_method
                return self.fail_result
        else:
            self.fail_result['message'] = '请求的响应状态码非%s'%str(code)
            return self.fail_result


if __name__ == '__main__':
    # checkutils = CheckUtils({"access_token":"35_BKh82IAvv_7Obcdwyre-v60qGrcS5rrWo-XN24oxrKZ4Xxh8OIcsa3FahcUsrB_6hY5zEXpx7adPDHNLkFGQuqJY80BHsZc8fIXXkXiMTlvA-hZe5o_KJRlyyVnAXWsywtW5k9vw_1lZ-1IiINAdACAMRE","expires_in":7200})
    # print(checkutils.check_key('access_token,expires_in'))
    # print(checkutils.check_key_value('{"access_token":"35_BKh82IAvv_7Obcdwyre-v60qGrcS5rrWo-XN24oxrKZ4Xxh8OIcsa3FahcUsrB_6hY5zEXpx7adPDHNLkFGQuqJY80BHsZc8fIXXkXiMTlvA-hZe5o_KJRlyyVnAXWsywtW5k9vw_1lZ-1IiINAdACAMRE","expires_in":7200}'))
    checkutils = CheckUtils('{"access_token":"35_BKh82IAvv_7Obcdwyre-v60qGrcS5rrWo-XN24oxrKZ4Xxh8OIcsa3FahcUsrB_6hY5zEXpx7adPDHNLkFGQuqJY80BHsZc8fIXXkXiMTlvA-hZe5o_KJRlyyVnAXWsywtW5k9vw_1lZ-1IiINAdACAMRE","expires_in":7200}')
    print(checkutils.check_regexp('{"access_token":"(.+?)","expires_in":(.+?)}'))



