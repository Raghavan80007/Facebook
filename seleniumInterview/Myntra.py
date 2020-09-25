from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome('D://chromedriver//chromedriver.exe')
driver.get("https://www.myntra.com/")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_xpath("//input[@class='desktop-searchBar']").send_keys('adidas')
time.sleep(5)
driver.find_element_by_xpath("//a[@class='desktop-submit']").click()


# MouseHover.   
element_to_hover_over = driver.find_elements_by_xpath("//span[@class='desktop-userTitle']")
for mousehover in element_to_hover_over:
    if(mousehover.text=='Profile'):
        hover = ActionChains(driver).move_to_element(mousehover)
        hover.perform()
        break

driver.find_element_by_xpath("//a[@class='desktop-linkButton']").click()
driver.find_element_by_xpath("//input[@type='tel']").send_keys(8886668007)
driver.find_element_by_xpath("//div[@class='submitBottomOption']").click()
password = driver.find_elements_by_xpath("//div[@class='bottomeLink']/span")
for pwd in password:
    if(pwd.text=='Password'):
        pwd.click()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("Akhil@007")
        driver.find_element_by_xpath("//button[@class='btn primary  lg block submitButton']").click()
    break
