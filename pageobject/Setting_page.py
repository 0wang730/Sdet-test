import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage


class SettingPage(BasePage):
    login_out_button = (By.XPATH, '//*[text()="Log out"]')
    profile_button = (By.XPATH, '//*[text()="Profile"]')
    edit_Profile = (By.XPATH, '//*[@class="em-button-base"]')
    birthday_button = (By.XPATH, '//*[@placeholder="DD / MM / YY"]')
    day_button = (By.XPATH, '//*[text()="22"]')
    OK_button = (By.XPATH, '//*[text()="OK"]')
    save_button = (By.XPATH, '//*[text()="Save"]')
    login_out_button1 = (By.XPATH, '//*[@class="MuiButtonBase-root css-1kcgzw2"]')

    def login_out(self):
        self.click(self.login_out_button)
        # print(self.login_out_button)
        self.click(self.login_out_button1)

    def profile_userInfo(self):
        self.click(self.profile_button)
        time.sleep(2)
        self.click(self.edit_Profile)
        time.sleep(2)
        self.click(self.birthday_button)
        time.sleep(2)
        self.click(self.day_button)
        time.sleep(2)
        self.click(self.OK_button)
        time.sleep(2)
        self.click(self.save_button)
        time.sleep(8)