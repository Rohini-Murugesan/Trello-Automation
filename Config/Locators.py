class TrelloLocators:
    USERNAME = "//input[@id='user']"
    PASSWORD = "//input[@id='password']"
    LOGIN_BUTTON = "//input[@id='login']"
    LOGIN_SUBMIT = '//button[@id="login-submit"]'
    CLICK_BOARD = '//div[@id="board"]'
    SHOW_MENU = "//span[text()='Show menu']"
    VALIDATE_LOGIN = "//div[@class='_2JvEWwSoJlzeFr']"

class BoardsLocator:
    CREATE_BOARD = "//div[@class='board-tile mod-add']"
    SELECT_BLUE_BACKGROUND = "//li[@class='_3XLlpTqqGMaaAG']/button[@title='blue']"
    BLUE_BACKGROUND = "//button[@title='blue']"
    CREATE_BOARD_INPUT = "//input[@placeholder='Add board title']"
    CREATE_BOARD_BUTTON = "//button[text()='Create board']"
    SELECT_MORE = "//a[contains(text(),'More')]"
    SELECT_CLOSE_BOARD = "//a[contains(text(),'Close board')]"
    CONFIRM_CLOSE = "//input[@value='Close' and contains(@class,'danger')]"
    SELECT_BOARD_DELETE = "//a[@class='quiet js-delete']"
    CONFIRM_BOARD_DELETE = "//input[@value='Delete' and contains(@class,'danger')]"

class CardsLocator:
    CREATE_CARD_A = '//h2[@class="list-header-name-assist js-list-name-assist" and text()="{{{LISTNAME}}}"]/parent::div/following-sibling::div[2]/a'
    ENTER_CARD_NAME = '//h2[@class="list-header-name-assist js-list-name-assist" and text()="{{{LISTNAME}}}"]/parent::div/following-sibling::div[1]//textarea'
    SUBMIT_CREATE_CARD = '//h2[@class="list-header-name-assist js-list-name-assist" and text()="{{{LISTNAME}}}"]/parent::div/following-sibling::div[1]//input[@type="submit"]'
    MEMBERS = '//a[@title="Members"]'
    CLOSE_CARD_MODAL = '//a[@class="icon-md icon-close dialog-close-button js-close-window"]'
    COMMENT_BOX = '//textarea[@class="comment-box-input js-new-comment-input"]'
    SAVE_COMMENT = '//input[@value="Save"]'
    SELECT_MOVE = '//input[@value="Move"]'
    MOVE_TO_SELECT = '//select[@class="js-select-list"]'
    SPAN_MOVE = '//span[text()="Move"]'

class ListsLocator:
    CREATE_LIST = "//span[@class='placeholder']"
    LIST_NAME_INPUT = "//input[@class='list-name-input' and @name='name']"
    CREATE_LIST_SUBMIT = "//input[@value='Add list']"
    VALIDATE_CREATED_LIST = '//h2[text()="{{{LISTNAME}}}"]'


