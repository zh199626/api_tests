import unittest
from HTMLTestRunner import HTMLTestRunner
from api.user_manager import UserManager
from setting import TEST_REPOST_PATH,LOGIN_INFO
h = UserManager()

if __name__ == '__main__':

    h.login(LOGIN_INFO.get('username'),LOGIN_INFO.get('password'))
    suite = unittest.TestLoader().discover('./cases','test*.py')

    with open(TEST_REPOST_PATH,'wb') as f:

        renner = HTMLTestRunner(f,title='测试报告')
        renner.run(suite)

