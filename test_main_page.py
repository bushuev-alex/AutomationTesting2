from .pages.main_page import MainPage
from .pages.locators import MainPageLocators

def test_guest_can_go_to_login_page(browser):
    link = MainPageLocators.LINK
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    link = MainPageLocators.LINK
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()