# coding:utf-8
import re
import jsonpath as jsonpath
import requests
import ast
from common.configutils import config_utils
from common.checkutils import CheckUtils


class RequestUtils:
    def __init__(self):
        self.host = config_utils.HOST
        self.session = requests.session()
        self.url = config_utils.HOST
        self.headers = {"ContentType": "application/json;charset=utf-8"}
        self.temp_variables = {}

    def __get(self, test_info):
        url = self.host + test_info['请求地址']
        # 将取出来的字符串数据去掉字符串标志，请求中需要上送的是字典形式
        params = ast.literal_eval(test_info['请求参数(get)'])
        req_get = self.session.get(url=url,
                                   params=params)
        req_get.encoding = req_get.apparent_encoding
        # 通过excel表中关联取值的方式获取关联的值放到一个临时字典中
        if test_info['取值方式'] == 'json取值':
            value = jsonpath.jsonpath(req_get.json(), test_info["取值代码"])[0]
            self.temp_variables[test_info["传值变量"]] = value
            # print(self.temp_variables)
        elif test_info['取值方式'] == '正则取值':
            value = re.findall(test_info["取值代码"], req_get.text)[0]
            self.temp_variables[test_info["传值变量"]] = value
            # print(self.temp_variables)
        result = CheckUtils(req_get).run_check(test_info['期望结果类型'],test_info['期望结果'])
        return result

    def __post(self, test_info):
        url = self.host + test_info['请求地址']
        # 将取出来的字符串数据去掉字符串标志，请求中需要上送的是字典形式
        param = ast.literal_eval(test_info['请求参数(get)'])
        data = test_info['提交数据（post）']
        # json = ast.literal_eval(test_info['提交数据（post）'])
        # data = data.encode("utf-8").decode("latin1")
        req_post = self.session.post(url=url,
                                     params=param,
                                     data=data,
                                     # json=json,
                                     headers=self.headers
                                     )
        """
        param参数的数据类型必须是字典类型，test_info['请求参数(get)']取出来的是'{{"access_token":${token}}}'"字符串格式，
        需要用ast.literal_eval转换一下
        data参数的数据类型要求是字符串格式
        json参数的数据类型要求是字典格式
        """
        req_post.encoding = req_post.apparent_encoding
        if test_info['取值方式'] == 'json取值':
            value = jsonpath.jsonpath(req_post.json(), test_info["取值代码"])[0]
            self.temp_variables[test_info["传值变量"]] = value
        elif test_info['取值方式'] == '正则取值':
            value = re.findall(test_info["取值代码"], req_post.text)[0]
            self.temp_variables[test_info["传值变量"]] = value
        req_post.encoding = req_post.apparent_encoding
        result = CheckUtils(req_post).run_check(test_info["期望结果类型"],test_info["期望结果"])
        return result

    # 将请求方式进行封装
    def request(self, test_info):
        # print(self.temp_variables)
        request_method = test_info['请求方式']
        param_variable_list = re.findall('\\${\w+}', test_info["请求参数(get)"])
        if param_variable_list:
            for param_variable in param_variable_list:
                # print('"%s"'%(self.temp_variables.get(param_variable[2:-1])))
                test_info["请求参数(get)"] = test_info["请求参数(get)"].replace(param_variable, '"%s"' % (
                    self.temp_variables.get(param_variable[2:-1])))
        if request_method == 'get':
            result = self.__get(test_info)
        elif request_method == 'post':
            data_variable_list = re.findall('\\${\w+}', test_info["提交数据（post）"])
            if data_variable_list:
                for data_variable in data_variable_list:
                    test_info["提交数据（post）"] = test_info["提交数据（post）"].replace(data_variable,
                                                                              '"%s"' % (self.temp_variables.get(
                                                                                  data_variable[2:-1])))
            result = self.__post(test_info)
        else:
            result = {'code': 1, 'result': '请求方式不支持'}
        return result

    # 封装一个案例多个步骤
    def test_steps(self, test_info):
        for step in test_info:
            result = self.request(step)
            if result['code'] != 0:
                break
            print(result)
        return result


if __name__ == '__main__':
    request_util = RequestUtils()
    case_info = [{'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'},
                 {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '删除标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag":{"id":408}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对', '期望结果': '{"errcode":0,"errmsg":"ok"}'}]
    case = request_util.test_steps(case_info)