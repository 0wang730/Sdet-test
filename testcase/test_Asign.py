import time

from base.DriverUtil import DriverUtil
from base.base_util import BaseUtils
from pageobject.Signup_page import SignupPage


class TaskCase(BaseUtils):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtil().start()
        cls.driver.maximize_window()

    def tearDownClass(cls):
        cls.driver.close()

    def test_sign(self):

        lp = SignupPage(self.driver)
        lp.to_sign()
        # time.sleep(8)
        lp.sign("", "") #the account you want to sign up
        time.sleep(2)