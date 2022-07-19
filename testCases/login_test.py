from selenium import webdriver
from pageObjects.LoginPage import Login

class Test_Login_001:




    def test_homepage_title(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.open_my_account_menu()
