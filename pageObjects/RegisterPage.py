from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_url(self, expected_url):
        current_url = self.driver.current_url
        if current_url == expected_url:
            print("URL verification passed. Current URL matches expected URL:", current_url)
            return True
        else:
            print("URL verification failed.")
            return False

    def fill_email_and_submit(self, email):
        js_script = """
            let firstShadowHost = document.querySelector("route-view)
            let firstShadowRoot = firstShadowHost.shadowRoot;
            let secondShadowHost = firstShadowRoot.querySelector("prospect-register-page");
            let secondShadowRoot = secondShadowHost.shadowRoot;
            let emailInput = secondShadowRoot.querySelector("input[type='email']");
            emailInput.value = '{}';
            let buttonSubmit = secondShadowRoot.querySelector("button[id='submit-button']");
            buttonSubmit.click();
        """.format(email)

        self.driver.execute_script(js_script)

