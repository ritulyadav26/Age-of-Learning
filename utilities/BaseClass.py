import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verify_url_presence(self, expected_url):
        try:
            element = WebDriverWait(self.driver, 5).until(EC.url_to_be(expected_url))
            return True
        except TimeoutException:
            return False