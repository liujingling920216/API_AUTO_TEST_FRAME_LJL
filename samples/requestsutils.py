#coding:utf-8
import re

import jsonpath as jsonpath
import requests
import ast
from  common.configutils import config_utils

class RequestUtils:
    def __init__(self):
        self.host = config_utils.HOST
        self.session = requests.session()
        self.url = config_utils.HOST
        self.headers = {"ContentType":"application/json;charset=utf-8"}
        self.temp_variables = {}

    def __get(self,test_info):
        url = self.host + test_info['请求地址']
        print(url)
        # 将取出来的字符串数据去掉字符串标志，请求中需要上送的是字典形式
        params = ast.literal_eval(test_info['请求参数(get)'])
        req_get = self.session.get(url= url,
                               params = params)
        req_get.encoding = req_get.apparent_encoding
        # 通过excel表中关联取值的方式获取关联的值放到一个临时字典中
        if test_info['取值方式']=='json取值':
            value = jsonpath.jsonpath(req_get.json(),test_info["取值代码"])[0]
            self.temp_variables[test_info["传值变量"]] = value
            # print(self.temp_variables)
        elif test_info['取值方式']=='正则取值':
            value = re.findall(test_info["取值代码"],req_get.text)[0]
            self.temp_variables[test_info["传值变量"]] = value
            # print(self.temp_variables)

        res_get = {
            'code':0,  #请求是否成功的标志位
            'response_reason':req_get.reason,
            'response_code':req_get.status_code,
            'response_headers':req_get.headers,
            'response_body':req_get.text
        }
        return res_get

    def __post(self,test_info):
        url = self.host + test_info['请求地址']
        # 将取出来的字符串数据去掉字符串标志，请求中需要上送的是字典形式
        params = ast.literal_eval(test_info['请求参数(get)'])
        # json = ast.literal_eval(test_info['提交数据（post）'])
        data = test_info['提交数据（post）']
        data=data.encode("utf-8").decode("latin1")
        req_post = self.session.post(url= url,
                               params = params,
                               data =data ,
                               headers = self.headers
                                )
        if test_info['取值方式']=='json取值':
            value = jsonpath.jsonpath(req_post.json(),test_info["取值代码"])[0]
            self.temp_variables[test_info["传值变量"]] = value
            # print(self.temp_variables)
        elif test_info['取值方式']=='正则取值':
            value = re.findall(test_info["取值代码"],req_post.text)[0]
            self.temp_variables[test_info["传值变量"]] = value
            # print(self.temp_variables)
        req_post.encoding = req_post.apparent_encoding
        res_post = {
            'code':0,  #请求是否成功的标志位
            'response_reason':req_post.reason,
            'response_code':req_post.status_code,
            'response_headers':req_post.headers,
            'response_body':req_post.text
        }
        return res_post

    # 将请求方式进行封装
    def request(self,test_info):
        request_method =  test_info['请求方式']
        if request_method == 'get':
            result = self.__get(test_info)
        elif request_method == 'post':
            result = self.__post(test_info)
        else:
            result = {'code':1,'result':'请求方式不支持'}
        return result

    # 封装一个案例多个步骤
    def test_steps(self,test_info):
        for step in test_info:
            result = self.request(step)
            if result['code'] != 0:
                break
            print(result['response_body'])
        return result['response_body']


if __name__ == '__main__':
    request_util = RequestUtils()
    request_util.test_steps([
        {
            '期望结果类型': '正则匹配',
            '请求方式': 'get',
            '请求地址': '/cgi-bin/token',
            '用例执行': '否',
            '测试用例编号': 'case02',
            '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}',
            '提交数据（post）': '',
            '取值方式': 'json取值',
            '测试用例名称': '测试能否正确新增用户标签',
            '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}',
            '取值代码': '$.access_token',
            '传值变量': 'token',
            '测试用例步骤': 'step_01',
            '接口名称': '获取access_token接口'
        },
        {
            '期望结果类型': '正则匹配',
            '请求方式': 'post',
            '请求地址': '/cgi-bin/tags/create',
            '用例执行': '否',
            '测试用例编号': 'case02',
            '期望结果': '{"tag":{"id":(.+?),"name":"衡东8888"}}',
            '提交数据（post）': '{"tag" : {"name" : "衡东8888"}}',
            '取值方式': '无',
            '测试用例名称': '测试能否正确新增用户标签',
            '请求参数(get)': '{"access_token":"35_h3gykUAU6MR-tGGz_1AAKJVvG8ZZmVTP0wkLxLkj3M2hSvkK6Y_DSNEysaauNq6QDKo1PZL25Fl3RkvwHkGWXTfUsth0g1Z5OJDclaIE-Y-7Z2X2mqIC2x--r7Rr3EfZfbOdRGSvPvSqBUDWNZNgAFAYKY"}',
            '取值代码': '',
            '传值变量': '',
            '测试用例步骤': 'step_02',
            '接口名称': '创建标签接口'
        }])