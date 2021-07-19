from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    URL_TO_LOGIN_PAGE = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    URL_TO_MAIN_PAGE = "http://selenium1py.pythonanywhere.com/"


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
