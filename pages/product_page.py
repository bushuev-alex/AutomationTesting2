from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):

    def add_item_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_SELECTOR)
        link.click()

    def check_name_product_in_basket(self):
        name_prod = self.browser.find_element(*ProductPageLocators.PROD_NAME_SELECTOR).text
        name_prod_confirmation = self.browser.find_element(*ProductPageLocators.PROD_NAME_SELECTOR_CONFIRM).text
        assert name_prod == name_prod_confirmation, "Wrong product name"

    def check_price_product_in_basket(self):
        price_prod = self.browser.find_element(*ProductPageLocators.PROD_PRICE_SELECTOR).text
        price_prod_confirmation = self.browser.find_element(*ProductPageLocators.PROD_PRICE_SELECTOR_CONFIRMED).text
        assert price_prod == price_prod_confirmation, "Wrong product price"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
