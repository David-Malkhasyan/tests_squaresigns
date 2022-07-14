import time
import unittest
import XLUtils
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import Generator

driver = webdriver.Chrome()

driver.get("https://goodwin.am/am/")
driver.maximize_window()
driver.implicitly_wait(5)


driver.find_element(By.CLASS_NAME, ("login-button")).click()
email_field = driver.find_element(By.NAME, ("username"))
email_field.click()
email_field.send_keys()


time.sleep(5)
driver.close()


# class SSMainFlow(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#
#     def test_add_to_cart(self):
#         driver = self.driver
#         driver.maximize_window()
#         driver.implicitly_wait(2)
#
#         driver.get("https://staging.squaresigns.com/")
#         assert "Make your sign" in driver.title
#
#         hover = ActionChains(self.driver)
#         my_account_button = self.driver.find_element(By.CLASS_NAME, "signed-in")
#         login_link = self.driver.find_element(By.XPATH,
#                                               r"/html/body/div[1]/header/div/div/div[3]/div/div[2]/div/div[2]/ul/li[1]")
#
#         hover.move_to_element(my_account_button).move_to_element(login_link).click().perform()
#
#         time.sleep(0.5)
#
#         popup_login_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/form/button[1]")
#         popup_login_button.click()
#
#
#
#
#
