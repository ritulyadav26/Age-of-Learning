class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_signup_button_inside_shadow(self):
        js_script = """
            let firstShadowHost = document.querySelector("route-view)
            let firstShadowRoot = firstShadowHost.shadowRoot;
            let secondShadowHost = firstShadowRoot.querySelector("home-element");
            let secondShadowRoot = secondShadowHost.shadowRoot;
            let buttonInsideSecondShadow = secondShadowRoot.querySelector("signup-button[aria-label='Sign Up for ABCmouse.com']");
            buttonInsideSecondShadow.click();
        """
        self.driver.execute_script(js_script)