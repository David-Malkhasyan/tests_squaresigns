import time
import unittest
import XLUtils
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import Generator


class LoginTest(unittest.TestCase):

    def setUp(self):
        Generator.negative_random_generator_email()
        Generator.password()

        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Chrome(executable_path = r'C:\Users\david.malkhasyan\Desktop\PythonTesting\webdrivers')
        self.driver.get("https://staging.squaresigns.com/")

        self.driver.maximize_window()
        self.driver.implicitly_wait(0.5)

    def test_negative_cases(self, startpoint=2):

        test_data_file_path = r'C:\Users\david.malkhasyan\Desktop\PythonTesting\Data\Sign_In.xlsx'
        hover = ActionChains(self.driver)
        my_account_button = self.driver.find_element(By.CLASS_NAME, "signed-in")
        login_link = self.driver.find_element(By.XPATH,
                                              r"/html/body/div[1]/header/div/div/div[3]/div/div[2]/div/div[2]/ul/li[1]")

        hover.move_to_element(my_account_button).move_to_element(login_link).click().perform()

        time.sleep(0.5)

        signin_popup_exist = self.check_exists("/html/body/div[1]/div[3]/div")
        self.assertEqual(signin_popup_exist, True)

        sheet_rows = XLUtils.get_row_count(test_data_file_path, "Negative")




        for r in range(startpoint, sheet_rows + 1):

            username = XLUtils.read_data(test_data_file_path, "Negative", r, 1)
            if username is None:
                username = " "
            password = XLUtils.read_data(test_data_file_path, "Negative", r, 2)
            if password is None:
                password = " "

            input_email = self.driver.find_element(By.NAME, "signInEmail")
            input_email.clear()
            input_email.send_keys(username)


            input_password = self.driver.find_element(By.NAME, "password")
            input_password.clear()
            input_password.send_keys(password)

            focus_out_elem = self.driver.find_element(By.CLASS_NAME, "subtitle")
            focus_out_elem.click()

            email_error_message_exist = self.check_exists('/html/body/div[1]/div[3]/div/div/form/div[1]/div/h6')
            password_error_message_exist = self.check_exists('/html/body/div[1]/div[3]/div/div/form/div[2]/div/h6')

            popup_login_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/form/button[1]")
            popup_login_button.click()

            time.sleep(1)

            signin_popup_exist = self.check_exists("/html/body/div[1]/div[3]/div")

            if (email_error_message_exist or password_error_message_exist) is True and signin_popup_exist is True:
                XLUtils.write_data(test_data_file_path, "Negative", r, 3, "Passed")
            elif (email_error_message_exist or password_error_message_exist) is True and signin_popup_exist is False:
                self.driver.close()
                self.setUp()
                XLUtils.write_data(test_data_file_path, "Negative", r, 3, "Failed")
                startpoint = r + 1
                self.test_negative_cases(startpoint)
            elif (email_error_message_exist or password_error_message_exist) is False and signin_popup_exist is False:
                self.driver.close()
                self.setUp()
                XLUtils.write_data(test_data_file_path, "Negative", r, 3, "Login and Pass was valid, Logged in")
                startpoint = r + 1
                self.test_negative_cases(startpoint)
            elif (email_error_message_exist or password_error_message_exist) is False and signin_popup_exist is True\
                    and self.check_exists('//*[@id="react-app"]/div[4]/div/div/form/div[1]') is True:
                XLUtils.write_data(test_data_file_path, "Negative", r, 3,
                                   "Login and Pass wasn't valid, Not logged in passed")
            elif email_error_message_exist or password_error_message_exist or signin_popup_exist is None:
                XLUtils.write_data(test_data_file_path, "Negative", r, 3,
                                   "Null")
            else:
                self.driver.close()
                self.setUp()
                XLUtils.write_data(test_data_file_path, "Negative", r, 3, "Something went wrong")
                startpoint = r + 1
                self.test_negative_cases(startpoint)

        self.driver.close()

    # def test_positive_cases(self):
    #     pass

    # def tearDown(self):
    #     pass

    def check_exists(self, elem):
        #self.driver.implicitly_wait(0)

        try:
            self.driver.find_element(By.XPATH, elem)
            return True
        except NoSuchElementException:
            return False

        #self.driver.implicitly_wait(3)


if __name__ == "__main__":
    unittest.main()
