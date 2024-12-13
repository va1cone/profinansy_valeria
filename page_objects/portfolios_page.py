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
        self.create_portfolio_button_in_modal = (By.XPATH, create_portfolio_button_in_modal)
        self.created_regular_portfolio = (By.XPATH, created_regular_portfolio)
        self.portfolio_change = (By.XPATH, portfolio_change)
        self.delete_portfolio = (By.XPATH, delete_portfolio)
        self.delete_portfolio_in_modal = (By.XPATH, delete_portfolio_in_modal)

    @allure.step("Проверка на то, что текущий урл - https://frontend.test.profinansy.ru/market/portfolios")
    def wait_portfolios_url(self):
        self.assert_current_url(self.portfolios_url)

    @allure.step("Клик на кнопку создания портфеля")
    def click_create_portfolio_button(self):
        self.click(*self.create_portfolio_button)

    @allure.step("Ввод названия портфеля")
    def entering_name_portfolio(self):
        self.send_keys(*self.portfolio_name_input_field, name_portfolio)

    @allure.step("Клик на кнопку создания портфеля в модальном окне")
    def click_create_portfolio_button_in_modal(self):
        self.click(*self.create_portfolio_button_in_modal)

    @allure.step("Проверка создания портфеля по названию")
    def checking_the_creation_of_a_regular_portfolio(self):
        self.wait_until_visible(*self.created_regular_portfolio)

    @allure.step("Клик на три точки")
    def click_portfolio_change(self):
        self.click(*self.portfolio_change)

    @allure.step("Клик на кнопку удалить портфель")
    def click_delete_portfolio(self):
        self.click(*self.delete_portfolio)

    @allure.step("Клик на кнопку удалить портфель в модалке")
    def click_delete_portfolio_in_modal(self):
        self.click(*self.delete_portfolio_in_modal)

    @allure.step("Проверка появления модалки, что созданных портфелей нет")
    def checking_the_no_portfolios(self):
        self.wait_until_visible(*self.create_portfolio_button)

    @allure.step("Удаление портфеля")
    def delete_portfolio(self):
        self.click_portfolio_change()
        self.click_delete_portfolio()
        self.click_delete_portfolio_in_modal()
        self.checking_the_no_portfolios()