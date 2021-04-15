import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config.Locators import BoardsLocator
from Modules.Trello import Trello


class Boards(Trello, BoardsLocator):
    def __init__(self, driver, path):
        super().__init__(driver, path)
        super(BoardsLocator, self).__init__()

    def createBoard(self, boardName):
        try:
            status = False
            self.driver.find_element_by_xpath(self.CREATE_BOARD).click()
            create_board = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.SELECT_BLUE_BACKGROUND))
            )
            self.driver.find_element_by_xpath(self.BLUE_BACKGROUND).click()
            self.driver.find_element_by_xpath(self.CREATE_BOARD_INPUT).send_keys(boardName)
            time.sleep(2)
            self.driver.find_element_by_xpath(self.CREATE_BOARD_BUTTON).click()
            status = True
        except Exception as e:
            print("Exception in createBoard : ", e)
        finally:
            time.sleep(2)
            self.driver.save_screenshot(self.reportPath + '\\createBoard.png')
            return status

    def deleteBoard(self):
        try:
            status = False
            deleteXpathList = [self.SELECT_MORE, self.SELECT_CLOSE_BOARD, self.CONFIRM_CLOSE, self.SELECT_BOARD_DELETE,
                               self.CONFIRM_BOARD_DELETE]
            if self.is_visible(self.SHOW_MENU):
                deleteXpathList.insert(0, self.SHOW_MENU)
            for xpath in deleteXpathList:
                self.driver.find_element_by_xpath(xpath).click()
                time.sleep(0.5)
            status = True
        except Exception as e:
            print("Exception in deleteBoard : ", e)
        finally:
            time.sleep(1)
            self.driver.save_screenshot(self.reportPath + '\\deleteBoard.png')
            return status
