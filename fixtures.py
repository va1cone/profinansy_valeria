from page_objects.authorization_page import AuthorizationPage
from page_objects.home_page import HomePage
from data import *
from conftest import *

@pytest.fixture(scope="function")
def authorization_and_transition_portfolio(driver):
    authorization_page = AuthorizationPage(driver)
    authorization_page.opening_the_authorization_page()
    authorization_page.entering_email_in_the_login_form(test_email)
    authorization_page.entering_password_in_the_login_form(test_password)
    authorization_page.click_on_the_login_button()
    home_page = HomePage(driver)
    home_page.edit_cookie_1()
    home_page.edit_cookie_2()
    home_page.edit_cookie_3()
    authorization_page = AuthorizationPage(driver)
    authorization_page.open_portfolio_url()
