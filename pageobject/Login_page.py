import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):
    login_button = (By.XPATH, '/html/body/div/div[1]/div[2]/div[1]/a[2]/div')
    change_login_button = (By.XPATH, '/html/body/div/main/section/div/div/div/div[1]/p/a')
    username_button = (By.XPATH, '//*[@id="username"]')
    password_button = (By.XPATH, '//*[@id="password"]')
    action_button = (By.NAME, 'action')

    def to_login(self):

        self.click(self.login_button)

    def login(self, username, password):
        self.send_keys(self.username_button, username)
        self.send_keys(self.password_button, password)
        self.click(self.action_button)
