param_variable_list = ['${token}']
temp_variables = {"token":"35_Mg5QbOJpD7zq9z5hsw_YXzmE32cSbGBEgBXYrwMh-ruQGzJrCGHN4CZqs9Yy7YP8fW_0a6b5FPzzREdcPd7cMFR_8-eu6aTnWJfSSNQmTcSBP47DLPFrvhe1F_7d7eKlEk4cHjRa1T47j8dzLPYdAJARVE"}
test_info = {'请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag":{"id":459}}', '取值方式': '无', '传值变量': '', '取值代码': ''}


for param_variable in param_variable_list:
    print('"%s"' % (temp_variables.get(param_variable[2:-1])))
    print(test_info["请求参数(get)"])

    print(type(param_variable))
    print(type(test_info))
    print(param_variable)
    test_info["请求参数(get)"] = test_info["请求参数(get)"].replace(param_variable,"35_Mg5QbOJpD7zq9z5hsw_YXzmE32cSbGBEgBXYrwMh-ruQGzJrCGHN4CZqs9Yy7YP8fW_0a6b5FPzzREdcPd7cMFR_8-eu6aTnWJfSSNQmTcSBP47DLPFrvhe1F_7d7eKlEk4cHjRa1T47j8dzLPYdAJARVE")
    print(test_info["请求参数(get)"])
    test_info["请求参数(get)"] = test_info("请求参数(get)".replace(param_variable,'"%s"' % (temp_variables.get(param_variable[2:-1]))))
    print(test_info["请求参数(get)"])