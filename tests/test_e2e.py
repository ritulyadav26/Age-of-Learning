from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pageObjects.RegisterPage import RegisterPage
from pageObjects.SubscriptionPage import SubscriptionPage
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
import json

with open('config.json') as f:
    config = json.load(f)

register_url = config['urls']['register']
subscription_url = config['urls']['subscription']
email = config['email']
expected_text = config['text']


class TestOne(BaseClass):
    def test_e2e(self):
        self.driver.implicitly_wait(10)
        homepage = HomePage(self.driver)
        homepage.click_signup_button_inside_shadow()

        self.verify_url_presence(register_url)
        register_page = RegisterPage(self.driver)
        verification_result = register_page.verify_url(register_url)
        assert verification_result, "URL Verification failed."

        register_page.fill_email_and_submit(email)

        subs_page = SubscriptionPage(self.driver)
        self.verify_url_presence(subscription_url)

        verification_result1 = subs_page.verify_url1(subscription_url)
        assert verification_result1, "URL Verification failed."

        text_rendered = subs_page.is_text_rendered(expected_text)
        assert text_rendered, "Text not present on Subscription Page."

