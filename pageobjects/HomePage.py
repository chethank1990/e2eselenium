from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    searchBox = (By.XPATH, "//input[@class='search-keyword']")
    searchResults = (By.CSS_SELECTOR, "h4.product-name")
    addToCart = (By.XPATH, "//div[@class='product-action']/button")
    clickONCart = (By.CLASS_NAME, "cart-icon")
    proceedToCart = (By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]")

    inputname = (By.CSS_SELECTOR, "input[name='name']")
    inputemail = (By.NAME, "email")
    checkbox = (By.ID, "exampleCheck1")
    dropdownlist = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    successmessage = (By.CLASS_NAME, "alert-success")


    def getsearchBox(self):
        return self.driver.find_element(*HomePage.searchBox)

    def getsearchResults(self):
        return self.driver.find_elements(*HomePage.searchResults)

    def getaddToCart(self):
        return self.driver.find_elements(*HomePage.addToCart)

    def getclickONCart(self):
        return self.driver.find_element(*HomePage.clickONCart)

    def getproceedToCart(self):
        return self.driver.find_element(*HomePage.proceedToCart)

    def getinputname(self):
        return self.driver.find_element(*HomePage.inputname)

    def getinputemail(self):
        return self.driver.find_element(*HomePage.inputemail)

    def getcheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getdropdownlist(self):
        return self.driver.find_element(*HomePage.dropdownlist)

    def getsubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getsuccessmessage(self):
        return self.driver.find_element(*HomePage.successmessage)