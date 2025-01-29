# import pytest
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.remote.webelement import WebElement
# import time
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# from pageObjects.CheckoutPage import CheckOutPage
# from pageObjects.HomePage import HomePage
# from utilites.BaseClass import BaseClass
# # u can use (in) assert if alert msg is to big
# #@pytest.mark.usefixtures("setup")
# class TestOne(BaseClass):
#     def test_e2e(self):
#         homepage=HomePage(self.driver)
#         homepage.shopItems().click()
#         produts = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
#         for product in produts:
#             prouct_name = product.find_element(By.XPATH, "div/h4/a").text
#             if prouct_name == "Blackberry":
#
#                 product.find_element(By.XPATH, "div/button").click()
#
#         self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
#         self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
#
#         self.driver.find_element(By.ID, "country").send_keys("ind")
#         self.VerifyLinkPresence("India")
#         self.driver.find_element(By.LINK_TEXT, "India").click()
#         self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
#         self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
#         print(self.driver.find_element(By.CLASS_NAME, "alert-success").text)
#
#
#
