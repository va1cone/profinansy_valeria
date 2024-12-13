from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure
from page_objects.base_page import BasePage
from locators import *

class HomePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.investment_button_on_home_page = (By.XPATH, investment_button_on_home_page)
        self.portfolios_button_on_home_page = (By.XPATH, portfolios_button_on_home_page)

    @allure.step("Клик на кнопку инвестиции")
    def click_on_the_investment_button_on_home_page(self):
        self.click(*self.investment_button_on_home_page)

    @allure.step("Клик на кнопку портфели")
    def click_portfolios_button_on_home_page(self):
        self.click(*self.portfolios_button_on_home_page)

    def edit_cookie_1(self):
        self.driver.execute_script("window.localStorage.setItem('PERSONAL_MODAL_IDS', '[263]');")

    def edit_cookie_2(self):
        self.driver.execute_script("window.localStorage.setItem('watchedStories', '[14]');")

    def edit_cookie_3(self):
        self.driver.execute_script("window.localStorage.setItem('modal_informer_shown', 'true');")
