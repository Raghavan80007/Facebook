from selenium.webdriver.common.by import By


class Homepage:

    def __init__(self,driver):
        self.driver = driver

    profile = (By.XPATH,"//span[@class='desktop-userTitle']")
    login = (By.XPATH,"//a[@class='desktop-linkButton']")
    mobilenumber = (By.XPATH,"//input[@type='tel']")

    def Profile(self):
        return self.driver.find_elements(*Homepage.profile)

    def getLogin(self):
        return self.driver.find_element(*Homepage.login)

    def mobileNumber(self):
        return self.driver.find_element(*Homepage.mobilenumber)