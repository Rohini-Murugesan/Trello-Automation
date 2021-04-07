from Modules.Trello import Trello
from Config.Locators import ListsLocator

class List(Trello,ListsLocator):
    def __init__(self,driver):
        super().__init__(driver)
        super(ListsLocator,self).__init__()

    def createList(self, List):
        try:
            for i in List:
                self.driver.find_element_by_xpath(self.CREATE_LIST).click()
                self.driver.find_element_by_xpath(self.LIST_NAME_INPUT).send_keys(i)
                self.driver.find_element_by_xpath(self.CREATE_LIST_SUBMIT).click()
        except Exception as e:
            print("Exception in createList : ", e)



    def renameList(self ,renamingDetails):
        try:
            for x in renamingDetails:
                self.driver.find_element_by_xpath(
                    '//textarea[@class="list-header-name mod-list-name js-list-name-input" and text()="' + x[
                        'from'] + '"]/parent::div').click()
                self.driver.find_element_by_xpath('//textarea[@aria-label="' + x['from'] + '"]').send_keys('')
                self.driver.find_element_by_xpath('//textarea[@aria-label="' + x['from'] + '"]').send_keys(x['to'])
                self.driver.find_element_by_xpath(self.CLICK_BOARD).click()

        except Exception as e:
            print("Exception in renameList : ", e)

