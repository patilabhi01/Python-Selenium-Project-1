import inspect
import logging

import pytest
# from select import select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    # def VerifyLinkPresence(self,text):
    #
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def getLogger(self):
        loggerName=inspect.stack()[1][3]
        logger=logging.getLogger(loggerName)
        FileHandler = logging.FileHandler('logfile.log',encoding='utf-8')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        FileHandler.setFormatter(formatter)
        logger.addHandler(FileHandler)  # filehandler Object
        logger.setLevel(logging.DEBUG)
        return logger

    def selectOptionByText(self,locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
