import unittest
import paramunittest

# # 参数类型是元组
# @paramunittest.parametrized(
#     (3,3),
#     (7,4)
# )

# # 参数类型是列表
# @paramunittest.parametrized(
#     [3,3],
#     [7,4]
# )

# # 参数类型字典
# @paramunittest.parametrized(
#     {'numa' : 4,'numb' : 3},
#     {'numa' : 9,'numb' : 8}
# )

# 参数类型是个对象
# test_data = [{'numa' : 4,'numb' : 3},{'numa' : 9,'numb' : 8}]
# @paramunittest.parametrized(
#     *test_data
# )

# # 通过函数传入测试参数
def testdata():
    return [{'numa' : 4,'numb' : 3},{'numa' : 9,'numb' : 8}]
@paramunittest.parametrized(
    *testdata()
)

class TestDemo(unittest.TestCase):
    def setParameters(self,numa,numb):
        self.numa = numa
        self.numb = numb
    def test_case(self):
        print('%s和%s两个数进行比较'%(self.numa,self.numb))
        self.assertGreater(self.numa,self.numb)

if __name__ == '__main__':
    unittest.main()

# # 参数类型是元组
# @paramunittest.parametrized(
#     (3,3),
#     (7,4)
# )

# # 参数类型是列表
# @paramunittest.parametrized(
#     [3,3],
#     [7,4]
# )

# # 参数类型字典
# @paramunittest.parametrized(
#     {'numa' : 4,'numb' : 3},
#     {'numa' : 9,'numb' : 8}
# )

# 参数类型是个对象
# test_data = [{'numa' : 4,'numb' : 3},{'numa' : 9,'numb' : 8}]
# @paramunittest.parametrized(
#     *test_data
# )

# # 通过函数传入测试参数
# def testdata():
#     return [{'numa' : 4,'numb' : 3},{'numa' : 9,'numb' : 8}]

