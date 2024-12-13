from page_objects.authorization_page import AuthorizationPage
import allure
from data import *
from conftest import *

class TestAuthorizationPage:
    @allure.title("переход по клику на Конструктор»")
    def test_authorization(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(test_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        authorization_page.wait_home_url()