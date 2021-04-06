import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Modules import Trello

class Boards(Trello.Trello):
    def __init__(self,driver):
        super().__init__(driver)

    def createBoard(self,boardName):
        try:
            self.driver.find_element_by_xpath("//div[@class='board-tile mod-add']").click()
            create_board = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//li[@class='_3XLlpTqqGMaaAG']/button[@title='blue']"))
            )
            self.driver.find_element_by_xpath("//button[@title='blue']").click()
            self.driver.find_element_by_xpath("//input[@placeholder='Add board title']").send_keys(boardName)
            time.sleep(2)
            self.driver.find_element_by_xpath("//button[text()='Create board']").click()
        except Exception as e:
            print("Exception in createBoard : ", e)


    def deleteBoard(self):
        try:
            for xpath in ["//a[contains(text(),'More')]", "//a[contains(text(),'Close board')]",
                          "//input[@value='Close' and contains(@class,'danger')]", "//a[@class='quiet js-delete']",
                          "//input[@value='Delete' and contains(@class,'danger')]"]:
                self.driver.find_element_by_xpath(xpath).click()
                time.sleep(0.5)
        except Exception as e:
            print("Exception in deleteBoard : ", e)



