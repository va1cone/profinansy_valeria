from page_objects.authorization_page import AuthorizationPage
from page_objects.home_page import HomePage
from page_objects.portfolios_page import PortfoliosPage


def authorize_and_navigate_to_portfolios(driver, test_email, test_password):
    # Авторизация
    authorization_page = AuthorizationPage(driver)
    authorization_page.opening_the_authorization_page()
    authorization_page.entering_email_in_the_login_form(test_email)
    authorization_page.entering_password_in_the_login_form(test_password)
    authorization_page.click_on_the_login_button()

    # Перейти на главную страницу и редактировать куки
    home_page = HomePage(driver)
    home_page.edit_cookie_1()
    home_page.edit_cookie_2()
    home_page.edit_cookie_3()

    # Переход к портфелям
    home_page.click_on_the_investment_button_on_home_page()
    home_page.click_portfolios_button_on_home_page()

    # Переход на страницу портфелей
    portfolios_page = PortfoliosPage(driver)
    portfolios_page.wait_portfolios_url()