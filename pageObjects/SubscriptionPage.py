from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SubscriptionPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_url1(self, expected_url1):
        current_url1 = self.driver.current_url
        if current_url1 == expected_url1:
            print("URL verification passed. Current URL matches expected URL:", current_url1)
            return True
        else:
            print("URL verification failed.")
            return False

    def is_text_rendered(self, expected_text):
        page_source = self.driver.page_source
        if expected_text in page_source:
            print("Text '{}' is rendered on webpage.".format(expected_text))
            return True
        else:
            print("Text '{}' is not rendered on webpage.".format(expected_text))
            return False

