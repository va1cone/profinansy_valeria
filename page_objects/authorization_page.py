from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure
from page_objects.base_page import BasePage
from locators import *
from data import *



class AuthorizationPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.authorization_url = 'https://frontend.test.profinansy.ru/login'
        self.home_url = 'https://frontend.test.profinansy.ru/'
        self.portfolios_url = 'https://frontend.test.profinansy.ru/market/portfolios'
        self.input_login = (By.XPATH, input_login)
        self.input_password = (By.XPATH, input_password)
        self.button_submit = (By.XPATH, button_submit)

    @allure.step("Открытие страницы авторизации")
    def opening_the_authorization_page(self):
        self.open_page(self.authorization_url)

    @allure.step("Ввод почты")
    def entering_email_in_the_login_form(self, email: str):
        self.send_keys(*self.input_login, test_email)

    @allure.step("Ввод пароля")
    def entering_password_in_the_login_form(self, password: str):
        self.send_keys(*self.input_password, test_password)

    @allure.step("Клик на кнопку войти")
    def click_on_the_login_button(self):
        self.click(*self.button_submit)

    @allure.step("Проверка на то, что текущий урл - https://frontend.test.profinansy.ru/")
    def wait_home_url(self):
        self.assert_current_url(self.home_url)

    def open_portfolio_url(self):
        self.open_page(self.portfolios_url)
