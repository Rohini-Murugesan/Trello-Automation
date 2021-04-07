import time
from selenium.webdriver.support.select import Select
from Modules.Trello import Trello
from Config.Locators import CardsLocator

class Cards(Trello,CardsLocator):
    def __init__(self,driver):
        super().__init__(driver)
        super(CardsLocator,self).__init__()
    
    def createCards(self,cardsDetails):
        try:
            count = 0
            for card in cardsDetails:
                if count == 0:
                    self.driver.find_element_by_xpath(self.CREATE_CARD_A.replace("{{{LISTNAME}}}",card['listName'])).click()
                    count += 1
                self.driver.find_element_by_xpath(self.ENTER_CARD_NAME.replace("{{{LISTNAME}}}",card['listName'])).send_keys(card['cardName'])
                self.driver.find_element_by_xpath(self.SUBMIT_CREATE_CARD.replace("{{{LISTNAME}}}",card['listName'])).click()
                time.sleep(1)
            self.driver.find_element_by_xpath(self.CLICK_BOARD).click()
        except Exception as e:
            print("Exception in createCards : ", e)

    def assignCards(self,assignmentDetails):
        try:
            for assignDetails in assignmentDetails:
                self.driver.find_element_by_xpath("//h2[text()='" + assignDetails[
                    'listName'] + "']/parent::div/following-sibling::div[1]//span[@class='list-card-title js-card-name' and text()='" +
                                             assignDetails['cardName'] + "']").click()
                self.driver.find_element_by_xpath(self.MEMBERS).click()
                self.driver.find_element_by_xpath('//span[contains(@name,"'+assignDetails['assignTo']+'")]').click()
                time.sleep(1)
                self.driver.find_element_by_xpath(self.CLOSE_CARD_MODAL).click()
                time.sleep(1)
        except Exception as e:
            print("Exception in assignCards : ", e)

    
    def commentCards(self,commentDetailsList):
        try:
            for commentDetails in commentDetailsList:
                self.driver.find_element_by_xpath("//h2[text()='" + commentDetails[
                    'listName'] + "']/parent::div/following-sibling::div[1]//span[@class='list-card-title js-card-name' and text()='" +
                                             commentDetails['cardName'] + "']").click()
                self.driver.find_element_by_xpath(self.COMMENT_BOX).send_keys(
                    commentDetails['comment'])
                time.sleep(1)
                self.driver.find_element_by_xpath(self.SAVE_COMMENT).click()
                self.driver.find_element_by_xpath(self.CLOSE_CARD_MODAL).click()
        except Exception as e:
            print("Exception in commentCards : ", e)

    
    
    def moveCards(self,moveCardsDetails):
        try:
            for moveDetails in moveCardsDetails:
                self.driver.find_element_by_xpath("//h2[text()='" + moveDetails[
                    'listName'] + "']/parent::div/following-sibling::div[1]//span[@class='list-card-title js-card-name' and text()='" +
                                             moveDetails['cardName'] + "']").click()
                self.driver.find_element_by_xpath(self.SPAN_MOVE).click()
                Select(self.driver.find_element_by_xpath(self.MOVE_TO_SELECT)).select_by_visible_text(
                    moveDetails['moveTo'])
                self.driver.find_element_by_xpath(self.SELECT_MOVE).click()
                time.sleep(1)
                self.driver.find_element_by_xpath(self.CLOSE_CARD_MODAL).click()
                time.sleep(1.5)
        except Exception as e:
            print("Exception in moveCards : ", e)
        finally:
            return self.driver
