from selenium import webdriver


class DriverUtil():

    def __init__(self):
        self.driver = webdriver.Firefox()

    def start(self):
        self.driver.get('https://app.earnaha.com/profile/settings')
        # self.driver.get('https://www.baidu.com/')

        self.driver.implicitly_wait(15)
        # self.driver.maximize_window()
        return self.driver

    def stop(self):
        self.driver.quit()