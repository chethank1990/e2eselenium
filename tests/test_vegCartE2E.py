import time

import pytest

from pageobjects.CartPage import CartPage
from pageobjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestCartE2E(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        cartPage = CartPage(self.driver)

        homePage.getsearchBox().send_keys( "ber" )
        time.sleep( 4 )
        log.info("Printing the search results")
        veggieslist = homePage.getsearchResults()
        items = []
        for veggie in veggieslist:
            items.append( veggie.text )
        log.info( items )

        buttons = homePage.getaddToCart()
        for button in buttons:
            button.click()

        homePage.getclickONCart().click()

        homePage.getproceedToCart().click()
        time.sleep( 4 )

        log.info( "Printing the cart results" )
        cartveggieslist = cartPage.getCartVegsList()
        cartitems = []
        for cartveggie in cartveggieslist:
            cartitems.append( cartveggie.text )
        log.info( cartitems )
        assert items == cartitems
