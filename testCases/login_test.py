from selenium import webdriver
from pageObjects.LoginPage import Login

class Test_Login_001:
    baseURL = 'https://dev.squaresigns.com/'



    def test_homepage_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        title = self.driver.title
        self.driver.close()
        if title == "Make your sign online | Customize design and print with Square Signs":
            assert True
        else:
            assert False

