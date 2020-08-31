import pytest

from selenium import webdriver
from selenium.webdriver.support.select import Select

from pageobjects.HomePage import HomePage
from testdata.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_FillForm(self, getfillformdata):
        log = self.getLogger()
        testhomePage = HomePage(self.driver)
        log.info("First Name is "+getfillformdata["Firstname"])
        testhomePage.getinputname().send_keys(getfillformdata["Firstname"])
        log.info( "email id is " + getfillformdata["email"] )
        testhomePage.getinputemail().send_keys(getfillformdata["email"])
        testhomePage.getcheckbox().click()
        self.selectDropDown(testhomePage.getdropdownlist(),(getfillformdata["gender"]))
        testhomePage.getsubmit().click()
        message = testhomePage.getsuccessmessage().text
        assert "success" in message
        self.driver.refresh()


    @pytest.fixture(params= HomePageData.gettestdata("test1"))
    def getfillformdata(self,request):
        return request.param