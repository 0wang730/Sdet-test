
class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def locator_element(self, loc):
        return self.driver.find_element(*loc)

    def send_keys(self, loc, value):
        self.locator_element(loc).send_keys(value)

    def click(self, loc):
        self.locator_element(loc).click()

    def get_value(self, loc):
        return self.locator_element(loc).text

    def back(self):
        self.driver.back()
