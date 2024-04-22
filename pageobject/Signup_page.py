import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage


class SignupPage(BasePage):
    login_button = (By.XPATH, '/html/body/div/div[1]/div[2]/div[1]/a[1]/div')
    change_login_button = (By.XPATH, '/html/body/div/main/section/div/div/div/div[1]/p/a')
    username_button = (By.XPATH, '//*[@id="email"]')
    password_button = (By.XPATH, '//*[@id="password"]')
    action_button = (By.XPATH, '/html/body/div/main/section/div/div/div/form/div[3]/button')

    def to_sign(self):
        self.click(self.login_button)
    def sign(self, username, password):
        self.send_keys(self.username_button, username)
        self.send_keys(self.password_button, password)
        self.click(self.action_button)
