from page_objects.authorization_page import AuthorizationPage
from page_objects.home_page import HomePage
from data import *
from conftest import *
from URLS import *
import requests

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

@pytest.fixture
def create_portfolio():

    headers = {
        "Token": user_token
    }
    response = requests.post(ADD_PORTFOLIO, json={
        "title": "портфель",
        "wallet": "RUB",
        "created_date": "2024-12-25T14:10:07.069Z",
        "risk_profile": "careful",
        "init_transaction": 0
    }, headers=headers)
    assert response.status_code == 200
    response_json = response.json()
    assert "data" in response_json, "'data' not found in the response"
    assert "id" in response_json["data"], "'id' not found in 'data'"

    return response_json["data"]["id"]


@pytest.fixture
def create_and_delete_portfolio():
    headers = {"Token": user_token}
    response = requests.post(ADD_PORTFOLIO, json={
        "title": "портфель", "wallet": "RUB", "created_date": "2024-12-25T14:10:07.069Z",
        "risk_profile": "careful", "init_transaction": 0
    }, headers=headers)
    assert response.status_code == 200
    response_json = response.json()
    portfolio_id = response_json["data"]["id"]

    response = requests.post(DELETE_PORTFOLIO, json={"id": portfolio_id}, headers=headers)
    assert response.status_code == 200, f"Failed to delete portfolio {portfolio_id}"
