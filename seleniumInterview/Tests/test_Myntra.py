from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Utilities import BaseClass
from PageObjects import Profile
import time


class TestOne(BaseClass.Baseclass):
    def test_myntra(self):
        homepage = Profile.Homepage(self.driver)
        # MouseHover.
        element_to_hover_over = homepage.Profile()
        for mousehover in element_to_hover_over:
            if (mousehover.text == 'Profile'):
                hover = ActionChains(self.driver).move_to_element(mousehover)
                hover.perform()
                break

        homepage.getLogin().click()
        homepage.mobileNumber().send_keys(8886668007)
        self.driver.find_element_by_xpath("//div[@class='submitBottomOption']").click()
        password = self.driver.find_elements_by_xpath("//div[@class='bottomeLink']/span")
        for pwd in password:
            if (pwd.text == 'Password'):
                pwd.click()
                self.driver.find_element_by_xpath("//input[@type='password']").send_keys("Akhil@007")
                self.driver.find_element_by_xpath("//button[@class='btn primary  lg block submitButton']").click()
            break

