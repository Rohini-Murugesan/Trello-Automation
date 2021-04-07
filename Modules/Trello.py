import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config.Locators import TrelloLocators


def getChromeDriver():
    try:
        webDriver = webdriver.Chrome('D:\chromedriver\chromedriver.exe')
        webDriver.maximize_window()
        webDriver.implicitly_wait(15)
    except Exception as e:
        print("Exception in getChromeDriver : ", e)
    finally:
        return webDriver


class Trello(TrelloLocators):
    def __init__(self,driver):
        super(TrelloLocators,self).__init__()
        self.driver = driver

    def closeDriver(self):
        try:
            time.sleep(3)
            self.driver.quit()
        except Exception as e:
            print("Exception in closeDriver : ", e)

    def loginTrello(self):
        try:
            self.driver.get('https://trello.com/en/login')
            self.driver.find_element_by_xpath(self.USERNAME).send_keys('rohinimurugesan.23@gmail.com')
            self.driver.find_element_by_xpath(self.LOGIN_BUTTON).submit()
            time.sleep(10)  # need
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.PASSWORD ))
            )
            self.driver.find_element_by_xpath(self.PASSWORD).send_keys('testtrello123')
            self.driver.find_element_by_xpath(self.LOGIN_SUBMIT).submit()
        except Exception as e:
            print("Exception in loginTrello : ", e)

