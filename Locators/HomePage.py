from selenium.webdriver.common.by import By


class LoginLocators:

    my_account_menu = (By.XPATH, '//*[@id="react-app"]/header/div/div/div[3]/div/div[2]/div/div[1]/span')
    login_link = (By.XPATH, r'/html/body/div[1]/header/div/div/div[3]/div/div[2]/div/div[2]/ul/li[1]')
    signin_popup = (By.XPATH, '/html/body/div[1]/div[3]/div')
    email_input = (By.NAME, 'signInEmail')
    password_input = (By.NAME, 'password')
    popup_login_button = (By.XPATH, "/html/body/div[1]/div[3]/div/div/form/button[1]")