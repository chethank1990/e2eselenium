from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
    CartVegsList = (By.CSS_SELECTOR , "p.product-name")


    def getCartVegsList(self):
        return self.driver.find_elements(*CartPage.CartVegsList)
