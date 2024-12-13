from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure
from page_objects.base_page import BasePage
from locators import *
from data import *

class PortfoliosPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.portfolios_url = 'https://frontend.test.profinansy.ru/market/portfolios'
        self.create_portfolio_button = (By.XPATH, create_portfolio_button)
        self.portfolio_name_input_field = (By.XPATH, portfolio_name_input_field)

    @allure.step("Проверка на то, что текущий урл - https://frontend.test.profinansy.ru/market/portfolios")
    def wait_portfolios_url(self):
        self.assert_current_url(self.portfolios_url)

    def click_create_portfolio_button(self):
        self.click(*self.create_portfolio_button)

    def entering_name_portfolio(self):
        self.send_keys(*self.portfolio_name_input_field, name_portfolio)