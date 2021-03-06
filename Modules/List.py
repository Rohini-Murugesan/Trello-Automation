from Modules.Trello import Trello
from Config.Locators import ListsLocator

class List(Trello,ListsLocator):
    def __init__(self,driver,path):
        super().__init__(driver,path)
        super(ListsLocator,self).__init__()

    def createList(self, List):
        try:
            status = False
            for i in List:
                self.driver.find_element_by_xpath(self.CREATE_LIST).click()
                self.driver.find_element_by_xpath(self.LIST_NAME_INPUT).send_keys(i)
                self.driver.find_element_by_xpath(self.CREATE_LIST_SUBMIT).click()
                status = True
        except Exception as e:
            print("Exception in createList : ", e)
        finally:
            self.driver.save_screenshot(self.reportPath + '\\ListCreation.png')
            return status



    def renameList(self ,renamingDetails):
        try:
            status = False
            for x in renamingDetails:
                self.driver.find_element_by_xpath(
                    '//textarea[@class="list-header-name mod-list-name js-list-name-input" and text()="' + x[
                        'from'] + '"]/parent::div').click()
                self.driver.find_element_by_xpath('//textarea[@aria-label="' + x['from'] + '"]').send_keys('')
                self.driver.find_element_by_xpath('//textarea[@aria-label="' + x['from'] + '"]').send_keys(x['to'])
                self.driver.find_element_by_xpath(self.CLICK_BOARD).click()
                status = True
        except Exception as e:
            print("Exception in renameList : ", e)
        finally:
            self.driver.save_screenshot(self.reportPath + '\\List_Renaming.png')
            return status


