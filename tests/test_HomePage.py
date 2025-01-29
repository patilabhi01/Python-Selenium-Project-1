import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilites.BaseClass import BaseClass

class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log=self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is:"+ getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        log.info("last name is:" +getData["lastname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getExampleCheck().click()
        self.selectOptionByText(homepage.getGender(),getData["gender"])
        homepage.getSubmit().click()
        alretText=homepage.getSuccessMessage().text
        log.info("message recieved from application"+alretText)
        assert ("Success" in alretText)
        self.driver.refresh()



    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self,request):
        return request.param

