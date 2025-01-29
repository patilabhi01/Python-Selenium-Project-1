from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self,driver):
        self.driver=driver

    # driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    cardTitle =(By.XPATH,"//div[@class='card h-100']")
    cardfooter=(By.XPATH,"div/button")
    checkout=(By.XPATH,"//button[@class='btn btn-success']")
    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)
    def getCardfooter(self):
        return self.driver.find_elements(*CheckOutPage.cardfooter)
    def getcheckoutItems(self):
        return self.driver.find_element(*CheckOutPage.checkout)

