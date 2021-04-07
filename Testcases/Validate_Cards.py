from Modules import Trello, Boards, Cards, List
if __name__ == "__main__":
    # login
    driver = Trello.getChromeDriver()
    trelloObj = Trello.Trello(driver)
    boardsObj = Boards.Boards(driver)
    ListObj = List.List(driver)
    cardsObj = Cards.Cards(driver)

    trelloObj.loginTrello()

    # create board
    boardsObj.createBoard(boardName="Test")

    # create list
    ListObj.createList(['Test'])

    # Rename Lists
    renamingDetails = [{'from': 'To Do', 'to': 'Not Started'}, {'from': 'Done', 'to': 'In QA'},
                       {'from': 'Doing', 'to': 'In Progress'}, {'from': 'Test', 'to': 'Done'}]
    ListObj.renameList(renamingDetails)

    # Add cards
    cardsDetails = [{'listName': 'Not Started', 'cardName': 'Card 1'},
                    {'listName': 'Not Started', 'cardName': 'Card 2'},
                    {'listName': 'Not Started', 'cardName': 'Card 3'},
                    {'listName': 'Not Started', 'cardName': 'Card 4'}]
    cardsObj.createCards(cardsDetails)

    # assign cards
    assignmentDetails = [{'listName': 'Not Started', 'cardName': 'Card 1', 'assignTo': 'Rohini Murugesan'}]
    cardsObj.assignCards(assignmentDetails)

    # comment cards
    commentDetailsList = [{'listName': 'Not Started', 'cardName': 'Card 1', 'comment': 'I am Done'}]
    cardsObj.commentCards(commentDetailsList)

    # move cards
    moveCardsDetails = [{'listName': 'Not Started', 'cardName': 'Card 2', 'moveTo': 'In Progress'},
                        {'listName': 'Not Started', 'cardName': 'Card 3', 'moveTo': 'In QA'},
                        {'listName': 'In Progress', 'cardName': 'Card 2', 'moveTo': 'In QA'}]
    cardsObj.moveCards(moveCardsDetails)

    # delete board
    boardsObj.deleteBoard()

    # close driver
    trelloObj.closeDriver()
