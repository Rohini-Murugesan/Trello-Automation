import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config.Locators import TrelloLocators
from Config.Constants import *
from datetime import datetime
import os

def generateReportPath(testcaseName):
    path = DIRECTORY + "Reports\\" + datetime.now().strftime("%d_%m_%Y") + "\\" + testcaseName+ "\\" + datetime.now().strftime("%Hh_%Mm_%Ss")
    os.makedirs(path)
    return path

def getChromeDriver():
    try:
        webDriver = webdriver.Chrome(CHROME_DRIVER_PATH)
        webDriver.maximize_window()
        webDriver.implicitly_wait(15)
    except Exception as e:
        print("Exception in getChromeDriver : ", e)
    finally:
        return webDriver

class Trello(TrelloLocators):
    def __init__(self,driver,path):
        super(TrelloLocators,self).__init__()
        self.driver = driver
        self.reportPath = path

    def closeDriver(self):
        try:
            time.sleep(3)
            self.driver.quit()
        except Exception as e:
            print("Exception in closeDriver : ", e)

    def is_visible(self, locator):
        try:
            Elm = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH,locator)))
            return bool(Elm)
        except Exception as e:
            print("Exception in is_visible : ", e)

    def updateTestcaseResults(self,Testcase_Results):
        try:
            Testcase_Results['Result'] = "FAIL" if len(
                list(filter(lambda step: step[2] == False, Testcase_Results['Steps']))) > 0 else "PASS"
            files = [file for file in os.listdir(self.reportPath) if (file.lower().endswith('.png'))]
            cwd = os.getcwd()
            os.chdir(self.reportPath)
            files.sort(key=os.path.getmtime)
            Testcase_Results['Images'] = files
            os.chdir(cwd)
            return Testcase_Results
        except Exception as e:
            print("Exception in updateTestcaseResults : ", e)

    def loginTrello(self):
        try:
            status = False
            self.driver.get(TRELLO_LOGIN_URL)
            self.driver.find_element_by_xpath(self.USERNAME).send_keys(USERNAME)
            self.driver.find_element_by_xpath(self.LOGIN_BUTTON).submit()
            time.sleep(10)  # need
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.PASSWORD ))
            )
            self.driver.find_element_by_xpath(self.PASSWORD).send_keys(PASSWORD)
            self.driver.find_element_by_xpath(self.LOGIN_SUBMIT).submit()
            # Validate Login
            if self.is_visible(self.VALIDATE_LOGIN):
                print("Login is success")
                status = True
            else:
                print("Login failed")
        except Exception as e:
            print("Exception in loginTrello : ", e)
        finally:
            self.driver.save_screenshot(self.reportPath + '\\Login.png')
            return status

