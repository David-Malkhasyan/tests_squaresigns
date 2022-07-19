import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Locators.HomePage import LoginLocators
from testCases import conftest


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.hover_element = ActionChains(self.driver)

    # Hover on SignIn dropdown menu to open it
    def open_my_account_menu(self, ):
        my_account_menu = self.driver.find_element(*LoginLocators.my_account_menu)
        self.hover_element.move_to_element(my_account_menu)

    def click_on_signin_link(self, ):
        self.driver.find_element(*LoginLocators.login_link).click()

    def set_user_email(self, user_email):
        self.driver.find_element(*LoginLocators.email_input).send_keys(user_email)

    def set_user_password(self, password):
        self.driver.find_element(*LoginLocators.password_input).send_keys(password)

    def click_on_signin_function(self):
        self.driver.find_element(*LoginLocators.popup_login_button).click()
