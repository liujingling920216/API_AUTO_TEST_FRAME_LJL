from common.excelutil import ExcelUtils

# lista = ExcelUtils('Sheet1').get_sheet_data_by_dic()
list1 = [{
	'测试用例编号': 'case01',
	'测试用例名称': '测试能否正确执行获取access_token接口',
	'测试用例步骤': 'step_01'
}, {
	'测试用例编号': 'case02',
	'测试用例名称': '测试能否正确新增用户标签',
	'测试用例步骤': 'step_01'
}, {
	'测试用例编号': 'case02',
	'测试用例名称': '测试能否正确新增用户标签',
	'测试用例步骤': 'step_02'
}, {
	'测试用例编号': 'case03',
	'测试用例名称': '测试能否正确删除用户标签',
	'测试用例步骤': 'step_01'
}, {
	'测试用例编号': 'case03',
	'测试用例名称': '测试能否正确删除用户标签',
	'测试用例步骤': 'step_02'
}]





dic = {}
for n in list1:
    dic.setdefault(n["测试用例编号"], []).append(n)
"""
{
	'case01': [{
		'测试用例编号': 'case01',
		'测试用例名称': '测试能否正确执行获取access_token接口',
		'测试用例步骤': 'step_01'
	}],
	'case02': [{
		'测试用例编号': 'case02',
		'测试用例名称': '测试能否正确新增用户标签',
		'测试用例步骤': 'step_01'
	}, {
		'测试用例编号': 'case02',
		'测试用例名称': '测试能否正确新增用户标签',
		'测试用例步骤': 'step_02'
	}],
	'case03': [{
		'测试用例编号': 'case03',
		'测试用例名称': '测试能否正确删除用户标签',
		'测试用例步骤': 'step_01'
	}, {
		'测试用例编号': 'case03',
		'测试用例名称': '测试能否正确删除用户标签',
		'测试用例步骤': 'step_02'
	}]
}
"""




list2 = []
for k,v in dic.items():
    dict2 = {}
    dict2['test_case']= k
    dict2['test_info']= v
    list2.append(dict2)
print(list2)


