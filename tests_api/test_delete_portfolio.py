import requests
import allure
from URLS import *
from data import *
from fixtures import create_portfolio

class TestDeletePortfolio:

    @allure.title("Создание обычного портфеля")
    def test_create_usual_portfolio(self, create_portfolio):
        portfolio_id = create_portfolio
        assert portfolio_id is not None

    @allure.title("Удаление портфеля")
    def test_delete_portfolio(self, create_portfolio):
        portfolio_id = create_portfolio
        assert portfolio_id is not None

        headers = {
            "Token": user_token
        }

        response = requests.post(DELETE_PORTFOLIO, json={
            "id": portfolio_id
        }, headers=headers)

        assert response.status_code == 200
        assert response.json()["data"] is True
        assert response.json()["ok"] is True