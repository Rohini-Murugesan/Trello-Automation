import time
from selenium.webdriver.support.select import Select
from Modules.Trello import Trello
from Config.Locators import CardsLocator

class Cards(Trello,CardsLocator):
    def __init__(self,driver,path):
        super().__init__(driver,path)
        super(CardsLocator,self).__init__()
    
    def createCards(self,cardsDetails):
        try:
            status = False
            count = 0
            for card in cardsDetails:
                if count == 0:
                    self.driver.find_element_by_xpath(self.CREATE_CARD_A.replace("{{{LISTNAME}}}",card['listName'])).click()
                    count += 1
                self.driver.find_element_by_xpath(self.ENTER_CARD_NAME.replace("{{{LISTNAME}}}",card['listName'])).send_keys(card['cardName'])
                self.driver.find_element_by_xpath(self.SUBMIT_CREATE_CARD.replace("{{{LISTNAME}}}",card['listName'])).click()
                time.sleep(1)
            self.driver.find_element_by_xpath(self.CLICK_BOARD).click()
            status = True
        except Exception as e:
            print("Exception in createCards : ", e)
        finally:
            self.driver.save_screenshot(self.reportPath + '\\CreateCards.png')
            return status

    def assignCards(self,assignmentDetails):
        try:
            status = False
            for assignDetails in assignmentDetails:
                self.driver.find_element_by_xpath("//h2[text()='" + assignDetails[
                    'listName'] + "']/parent::div/following-sibling::div[1]//span[@class='list-card-title js-card-name' and text()='" +
                                             assignDetails['cardName'] + "']").click()
                self.driver.find_element_by_xpath(self.MEMBERS).click()
                self.driver.find_element_by_xpath('//span[contains(@name,"'+assignDetails['assignTo']+'")]').click()
                time.sleep(1)
                self.driver.save_screenshot(self.reportPath + '\\Assign'+assignDetails['cardName']+'To'+assignDetails['assignTo']+'.png')
                self.driver.find_element_by_xpath(self.CLOSE_CARD_MODAL).click()
                time.sleep(1)
            status = True
        except Exception as e:
            print("Exception in assignCards : ", e)
        finally:
            return status

    
    def commentCards(self,commentDetailsList):
        try:
            status = False
            for commentDetails in commentDetailsList:
                self.driver.find_element_by_xpath("//h2[text()='" + commentDetails[
                    'listName'] + "']/parent::div/following-sibling::div[1]//span[@class='list-card-title js-card-name' and text()='" +
                                             commentDetails['cardName'] + "']").click()
                self.driver.find_element_by_xpath(self.COMMENT_BOX).send_keys(
                    commentDetails['comment'])
                time.sleep(1)
                self.driver.find_element_by_xpath(self.SAVE_COMMENT).click()
                time.sleep(1)
                self.driver.save_screenshot(self.reportPath + '\\CommentAddedForCard'+commentDetails['cardName']+'.png')
                self.driver.find_element_by_xpath(self.CLOSE_CARD_MODAL).click()
            status = True
        except Exception as e:
            print("Exception in commentCards : ", e)
        finally:
            return status


    
    
    def moveCards(self,moveCardsDetails):
        try:
            status = False
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
                self.driver.save_screenshot(self.reportPath + '\\Move'+moveDetails['cardName']+'To'+moveDetails['moveTo']+'List.png')
                time.sleep(1.5)
            status = True
        except Exception as e:
            print("Exception in moveCards : ", e)
        finally:
            return status
