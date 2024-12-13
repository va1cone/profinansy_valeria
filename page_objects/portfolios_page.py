from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure
from page_objects.base_page import BasePage
from locators import *

class PortfoliosPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.portfolios_url = 'https://frontend.test.profinansy.ru/market/portfolios'

    @allure.step("Проверка на то, что текущий урл - https://frontend.test.profinansy.ru/market/portfolios")
    def wait_portfolios_url(self):
        self.assert_current_url(self.portfolios_url)
