from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage
from time import sleep


def test_add_item_to_basket(browser):
    link = ProductPageLocators.URL_TO_PROD_PAGE
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.check_name_product_in_basket()
    page.check_price_product_in_basket()
