import time
from selenium.webdriver.support.select import Select
from Modules import Trello

class Cards(Trello.Trello):
    def __init__(self,driver):
        super().__init__(driver)
    
    def createCards(self,cardsDetails):
        try:
            count = 0
            for card in cardsDetails:
                if count == 0:
                    self.driver.find_element_by_xpath('//h2[@class="list-header-name-assist js-list-name-assist" and text()="' + card[
                        'listName'] + '"]/parent::div/following-sibling::div[2]/a').click()
                    count += 1
                self.driver.find_element_by_xpath('//h2[@class="list-header-name-assist js-list-name-assist" and text()="' + card[
                    'listName'] + '"]/parent::div/following-sibling::div[1]//textarea').send_keys(card['cardName'])
                self.driver.find_element_by_xpath('//h2[@class="list-header-name-assist js-list-name-assist" and text()="' + card[
                    'listName'] + '"]/parent::div/following-sibling::div[1]//input[@type="submit"]').click()
                time.sleep(1)
            self.driver.find_element_by_xpath('//div[@id="board"]').click()
        except Exception as e:
            print("Exception in createCards : ", e)

    def assignCards(self,assignmentDetails):
        try:
            for assignDetails in assignmentDetails:
                self.driver.find_element_by_xpath("//h2[text()='" + assignDetails[
                    'listName'] + "']/parent::div/following-sibling::div[1]//span[@class='list-card-title js-card-name' and text()='" +
                                             assignDetails['cardName'] + "']").click()
                self.driver.find_element_by_xpath('//a[@title="Members"]').click()
                self.driver.find_element_by_xpath('//span[contains(@name,"'+assignDetails['assignTo']+'")]').click()
                time.sleep(1)
                self.driver.find_element_by_xpath('//a[@class="icon-md icon-close dialog-close-button js-close-window"]').click()
                time.sleep(1)
        except Exception as e:
            print("Exception in assignCards : ", e)

    
    def commentCards(self,commentDetailsList):
        try:
            for commentDetails in commentDetailsList:
                self.driver.find_element_by_xpath("//h2[text()='" + commentDetails[
                    'listName'] + "']/parent::div/following-sibling::div[1]//span[@class='list-card-title js-card-name' and text()='" +
                                             commentDetails['cardName'] + "']").click()
                self.driver.find_element_by_xpath('//textarea[@class="comment-box-input js-new-comment-input"]').send_keys(
                    commentDetails['comment'])
                time.sleep(1)
                self.driver.find_element_by_xpath('//input[@value="Save"]').click()
                self.driver.find_element_by_xpath('//a[@class="icon-md icon-close dialog-close-button js-close-window"]').click()
        except Exception as e:
            print("Exception in commentCards : ", e)

    
    
    def moveCards(self,moveCardsDetails):
        try:
            for moveDetails in moveCardsDetails:
                self.driver.find_element_by_xpath("//h2[text()='" + moveDetails[
                    'listName'] + "']/parent::div/following-sibling::div[1]//span[@class='list-card-title js-card-name' and text()='" +
                                             moveDetails['cardName'] + "']").click()
                self.driver.find_element_by_xpath('//span[text()="Move"]').click()
                Select(self.driver.find_element_by_xpath('//select[@class="js-select-list"]')).select_by_visible_text(
                    moveDetails['moveTo'])
                self.driver.find_element_by_xpath('//input[@value="Move"]').click()
                time.sleep(1)
                self.driver.find_element_by_xpath('//a[@class="icon-md icon-close dialog-close-button js-close-window"]').click()
                time.sleep(1.5)
        except Exception as e:
            print("Exception in moveCards : ", e)
        finally:
            return self.driver
