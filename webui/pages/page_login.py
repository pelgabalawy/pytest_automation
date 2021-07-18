import time
from seleniumpagefactory.Pagefactory import PageFactory
from _shared.custom_logger import logger


class Login_page(PageFactory):
    url = None

    def __init__(self,driver):
        # It is necessary to to initialise driver as page class member to implement Page Factory
        self.driver = driver

    # define locators dictionary where key name will became WebElement using PageFactory
    locators = {
        "edtUserName": ('ID', 'user_login'),
        "edtPassword": ('NAME', 'pwd'),
        "btnSignIn": ('XPATH', '//input[@value="Log In"]'),
        "lnkPost": ('XPATH', '//div[contains(text(),"Posts")]'),
        "lstAction": ('ID', 'bulk-action-selector-top')
    }

    def login(self, url, username, password):
        logger.info(f"url: {url}")
        logger.info(f"username: {username}")
        logger.info(f"password: {password}")
        self.driver.get(url)
        time.sleep(2)