import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def getChromeDriver():
    try:
        webDriver = webdriver.Chrome(
            'D:\chromedriver\chromedriver.exe')  # Optional argument, if not specified will search path.
        webDriver.maximize_window()
        webDriver.implicitly_wait(15)
    except Exception as e:
        print("Exception in getChromeDriver : ", e)
    finally:
        return webDriver

class Trello():
    def __init__(self,driver):
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
            self.driver.find_element_by_xpath("//input[@id='user']").send_keys('rohinimurugesan.23@gmail.com')
            self.driver.find_element_by_xpath("//input[@id='login']").submit()
            time.sleep(10)  # need
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
            )
            self.driver.find_element_by_xpath("//input[@id='password']").send_keys('testtrello123')
            self.driver.find_element_by_xpath('//button[@id="login-submit"]').submit()
        except Exception as e:
            print("Exception in loginTrello : ", e)

