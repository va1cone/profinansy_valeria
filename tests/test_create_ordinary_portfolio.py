from page_objects.portfolios_page import PortfoliosPage
import allure
from conftest import *
from fixtures import authorization_and_transition_portfolio



class TestCreateOrdinaryPortfolio:
    @allure.title("Создание обычного портфеля, Российский рубль, Осторожный, 0, дата не менялась, влияет на мой капитал")
    def test_create_ordinary_portfolio(self, driver, authorization_and_transition_portfolio):
        portfolio_page = PortfoliosPage(driver)
        portfolio_page.click_create_portfolio_button()
        portfolio_page.entering_name_portfolio()









