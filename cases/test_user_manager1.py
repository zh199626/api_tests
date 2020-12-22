
import unittest
from api.user_manager import UserManager
from data.user_manager_data import UserManagerData

class TestUserManagerCase(unittest.TestCase):

    user_id = None

    # 初始化方法
    @classmethod
    def setUpClass(cls) -> None:
        cls.user = UserManager()
        # cls.user.login('admin123','admin123')

        um = UserManagerData()

        cls.username = um.user_case_data.get('username')
        cls.password = um.user_case_data.get('password')
        cls.new_username = um.user_case_data.get('new_username')
        cls.new_password = um.user_case_data.get('new_password')
        # cls.username = cls.password = 'testzxc2'
        # cls.new_username = cls.new_password = 'testzxc'


    # case1 ：只输入用户名和密码进行添加管理员
    def test01_normal_add(self):

        # # 定义测试用例数据
        # username = 'testqwe29'
        # password = '123456'

        # 1.请求添加管理员接口
        actual_result = self.user.add_user(self.username,self.password)
        print(actual_result)
        data = actual_result.get('data')
        if data:
            TestUserManagerCase.user_id = data.get('id')
        # 2.对返回结果数据校验
        self.assertEqual(0,actual_result['errno'])
        self.assertEqual(self.username,data.get('username'))

        # case2 :编辑用户
    def test02_edit(self):
        # new_user_name  = new_user_password = 'testzxc'
        edit_result = self.user.edit_user(TestUserManagerCase.user_id,self.new_username,password=self.new_password)

        self.assertEqual(0, edit_result['errno'])
        self.assertEqual(self.new_username, edit_result['data']['username'])


        # 查询用户
    def test03_search(self):

        search_result = self.user.search_user()
        self.assertEqual(0, search_result['errno'])
        self.assertEqual(self.new_username,search_result.get('data').get('list')[0].get('username'))

        # case4 :删除用户
    def test04_delete(self):

        # 1.定义测试用例中的数据
        #
        # 2.调用被测接口
        dele_result = self.user.del_user(TestUserManagerCase.user_id)

        # 3.断言
        self.assertEqual(0,dele_result['errno'])



if __name__ == '__main__':
    unittest.main()



