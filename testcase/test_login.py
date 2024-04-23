import time

from base.DriverUtil import DriverUtil
from base.base_util import BaseUtils
from pageobject.Login_page import LoginPage
from pageobject.Setting_page import SettingPage
from pageobject.Signup_page import SignupPage


class TaskCase(BaseUtils):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil().start()
        cls.driver.maximize_window()

    def test_1login(self):
        lp = LoginPage(self.driver)
        lp.to_login()
        lp.login("812204941@qq.com", "12345678Abc!")#the account you want to sign in
        # lp.login_out()

    def test_2edit_userInfo(self):
        lp = SettingPage(self.driver)
        lp.profile_userInfo()

    def test_3log_out(self):
        lp = SettingPage(self.driver)
        lp.login_out()
        time.sleep(2)

    def tearDownClass(cls):
        cls.driver=DriverUtil.stop()