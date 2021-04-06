from Modules import Trello

class List(Trello.Trello):
    def __init__(self,driver):
        super().__init__(driver)

    def createList(self, List):
        try:
            for i in List:
                self.driver.find_element_by_xpath("//span[@class='placeholder']").click()
                self.driver.find_element_by_xpath("//input[@class='list-name-input' and @name='name']").send_keys(i)
                self.driver.find_element_by_xpath("//input[@value='Add list']").click()
        except Exception as e:
            print("Exception in createList : ", e)



    def renameList(self ,renamingDetails):
        try:
            # renamingDetails = [{'from': 'To Do', 'to': 'Not Started'}, {'from': 'Done', 'to': 'In QA'},
            #           {'from': 'Doing', 'to': 'In Progress'}, {'from': 'Test', 'to': 'Done'}]
            for x in renamingDetails:
                self.driver.find_element_by_xpath(
                    '//textarea[@class="list-header-name mod-list-name js-list-name-input" and text()="' + x[
                        'from'] + '"]/parent::div').click()
                self.driver.find_element_by_xpath('//textarea[@aria-label="' + x['from'] + '"]').send_keys('')
                self.driver.find_element_by_xpath('//textarea[@aria-label="' + x['from'] + '"]').send_keys(x['to'])
                self.driver.find_element_by_xpath('//div[@id="board"]').click()

        except Exception as e:
            print("Exception in renameList : ", e)

