from page_objects.portfolios_page import PortfoliosPage
import allure
from conftest import *
from fixtures import authorization_and_transition_portfolio



class TestDeletePortfolio:
    @allure.title("Создание обычного портфеля, Российский рубль, Осторожный, 0, дата не менялась, влияет на мой капитал")
    def test_delete_portfolio(self, driver, authorization_and_transition_portfolio):
        portfolio_page = PortfoliosPage(driver)
        #portfolio_page.click_create_portfolio_button()
        #portfolio_page.entering_name_portfolio()
        #portfolio_page.click_create_portfolio_button_in_modal()
        #portfolio_page.checking_the_creation_of_a_regular_portfolio()
        portfolio_page.click_portfolio_change()
        portfolio_page.click_delete_portfolio()
        portfolio_page.click_delete_portfolio_in_modal()
        portfolio_page.checking_the_no_portfolios()
