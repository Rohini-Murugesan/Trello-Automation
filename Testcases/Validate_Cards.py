import time

from Modules import Trello, Boards, Cards, List,Report
import json
start_time = time.time()

## Testcase Details
Testcase_Results = {'testcaseName': "Validate_Cards",
                    'testcaseDescription': "This testcase validates the Trello login and basic cards functionalities such as rename, move and assign cards"}

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


def Test():
    try:
        Testcase_Results['Steps'] = []
        # ***************************************************************
        # Step 1 : Validate login
        # ***************************************************************
        loginStatus = trelloObj.loginTrello()
        Testcase_Results['Steps'].append([1, "Validate Trello login", loginStatus])

        # ***************************************************************
        # Step 2 : Create a board named Test
        # ***************************************************************
        createBoardStatus = boardsObj.createBoard(boardName="Test")
        Testcase_Results['Steps'].append([2, "Create a board named Test", createBoardStatus])

        # ***************************************************************
        # Step 3: Create lists - Not Started, In Progress, In QA and Done
        # ***************************************************************
        createListStatus = ListObj.createList(['Test'])
        renameListStatus = ListObj.renameList(renamingDetails)
        Testcase_Results['Steps'].append(
            [3, "Create lists - Not Started, In Progress, In QA and Done", createListStatus and renameListStatus])

        # *****************************************************************************
        # Step 4 : Create cards - Card 1, Card 2, Card 3 and Card 4 under "Not Started"
        # *****************************************************************************
        createCardsStatus = cardsObj.createCards(cardsDetails)
        Testcase_Results['Steps'].append(
            [4, 'Create cards - Card 1, Card 2, Card 3 and Card 4 under "Not Started"', createCardsStatus])

        # **************************************************************************
        # Step 5 : Assign Card 1 to logged in member and comment 'I'm Done' in Card 1
        # **************************************************************************
        assignCardsStatus = cardsObj.assignCards(assignmentDetails)
        commentCardsStatus = cardsObj.commentCards(commentDetailsList)
        Testcase_Results['Steps'].append([5, "Assign Card 1 to logged in member and comment 'I'm Done' in Card 1",
                                          assignCardsStatus and commentCardsStatus])

        # *************************************************************************
        # Step 6 : Move Card 2 to In Progress, Card 3 to In QA and Card 2 to In QA
        # *************************************************************************
        moveCardsStatus = cardsObj.moveCards(moveCardsDetails)
        Testcase_Results['Steps'].append(
            [6, " Move Card 2 to In Progress, Card 3 to In QA and Card 2 to In QA", moveCardsStatus])

    except Exception as e:
        print("Exception in Test : ", e)
    finally:
        # ***************************************************************
        # Step 7 : Delete Board - Clean up
        # ***************************************************************
        deleteBoardStatus = boardsObj.deleteBoard()
        trelloObj.closeDriver()
        Testcase_Results['Steps'].append([7, "Delete the board", deleteBoardStatus])


if __name__ == "__main__":
    try:
        # Setup
        path = Trello.generateReportPath(Testcase_Results['testcaseName'])
        driver = Trello.getChromeDriver()
        trelloObj = Trello.Trello(driver, path)
        boardsObj = Boards.Boards(driver, path)
        ListObj = List.List(driver, path)
        cardsObj = Cards.Cards(driver, path)
        # Run Test
        Test()
    except Exception as e:
        print("Exception in __main__ : ", e)
    finally:
        # Update Results
        Testcase_Results = trelloObj.updateTestcaseResults(Testcase_Results)
        Testcase_Results['Date'] = path.split("\\")[-3]
        Testcase_Results['Time'] = path.split("\\")[-1]
        Testcase_Results['Execution_Time'] = time.time() - start_time
        print(Testcase_Results)
        with open(path + "\\report.js", "w") as outfile:
            outfile.write(("""let data = """ + str(json.dumps(Testcase_Results)).strip()))
        print("Find testcase artifacts in path : " + path)
        Report.generateReport(path, Testcase_Results)

