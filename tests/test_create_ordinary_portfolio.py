from page_objects.authorization_page import AuthorizationPage
from page_objects.home_page import HomePage
from page_objects.portfolios_page import PortfoliosPage
from test_help import authorize_and_navigate_to_portfolios
import allure
from data import *
from conftest import *

class TestCreateOrdinaryPortfolio:
    @allure.title("переход")
    def test_create_ordinary_portfolio(self, driver):
        authorize_and_navigate_to_portfolios(driver, test_email, test_password)




