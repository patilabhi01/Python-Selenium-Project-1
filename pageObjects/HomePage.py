from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver=driver
    # shop=(By.CSS_SELECTOR,"a[href*='shop']")
    name=(By.CSS_SELECTOR,"[name= 'name']")
    email=(By.NAME,"email")
    example_check=(By.ID,"exampleCheck1")
    gender=(By.ID,"exampleFormControlSelect1")
    submit=(By.XPATH,"//input [@value='Submit' ]")
    success_message=(By.CSS_SELECTOR,"[class*='alert-success']")


    # def shopItems(self):
    #     return self.driver.find_element(*HomePage.shop)
    #     #driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
    def getName(self):
        return self.driver.find_element(*HomePage.name)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    def getExampleCheck(self):
        return self.driver.find_element(*HomePage.example_check)
    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)
    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.success_message)