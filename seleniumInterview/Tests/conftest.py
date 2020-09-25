from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest


@pytest.fixture(scope='class')
def setUp(request):
    driver = webdriver.Chrome('D://chromedriver//chromedriver.exe')
    driver.get("https://www.myntra.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    request.cls.driver = driver
    yield
    driver.close()
