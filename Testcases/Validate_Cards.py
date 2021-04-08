from Modules import Trello, Boards, Cards, List
from datetime import datetime
now = datetime.now()
import os
from Config.Constants import DIRECTORY

## Testcase Details
testcaseName = "Validate_Cards"
testcaseDescription = "This testcase validates the Trello login and basic cards functionalities such as rename, move and assign cards"

path = DIRECTORY+"Reports\\"+now.strftime("%d_%m_%Y")+"\\"+testcaseName+"\\"+now.strftime("%Hh_%Mm_%Ss")
os.makedirs(path)


## Inputs
renamingDetails = [{'from': 'To Do', 'to': 'Not Started'}, {'from': 'Done', 'to': 'In QA'},
                   {'from': 'Doing', 'to': 'In Progress'}, {'from': 'Test', 'to': 'Done'}]
cardsDetails = [{'listName': 'Not Started', 'cardName': 'Card 1'},
                {'listName': 'Not Started', 'cardName': 'Card 2'},
                {'listName': 'Not Started', 'cardName': 'Card 3'},
                {'listName': 'Not Started', 'cardName': 'Card 4'}]
assignmentDetails = [{'listName': 'Not Started', 'cardName': 'Card 1', 'assignTo': 'Rohini Murugesan'}]
commentDetailsList = [{'listName': 'Not Started', 'cardName': 'Card 1', 'comment': 'I am Done'}]
moveCardsDetails = [{'listName': 'Not Started', 'cardName': 'Card 2', 'moveTo': 'In Progress'},
                    {'listName': 'Not Started', 'cardName': 'Card 3', 'moveTo': 'In QA'},
                    {'listName': 'In Progress', 'cardName': 'Card 2', 'moveTo': 'In QA'}]

if __name__ == "__main__":
    # login
    driver = Trello.getChromeDriver()
    trelloObj = Trello.Trello(driver,path)
    boardsObj = Boards.Boards(driver,path)
    ListObj = List.List(driver,path)
    cardsObj = Cards.Cards(driver,path)

    trelloObj.loginTrello()

    # create board
    boardsObj.createBoard(boardName="Test")

    # create list
    ListObj.createList(['Test'])

    # Rename Lists

    ListObj.renameList(renamingDetails)

    # Add cards

    cardsObj.createCards(cardsDetails)

    # assign cards
    cardsObj.assignCards(assignmentDetails)

    # comment cards

    cardsObj.commentCards(commentDetailsList)

    # Move cards
    cardsObj.moveCards(moveCardsDetails)

    # delete board
    boardsObj.deleteBoard()

    # close driver
    trelloObj.closeDriver()

print("Find testcase artifacts in path : "+path)