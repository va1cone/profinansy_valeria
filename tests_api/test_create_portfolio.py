import requests
import allure
from URLS import *
from data import *


class TestCreatePortfolio:

    @allure.title("Создание обычного портфеля")
    def test_create_usual_portfolio(self):
        headers = {
            "Token": user_token
        }

        response = requests.post(ADD_PORTFOLIO, json={
            "title": "обычный портфель",
            "wallet": "RUB",
            "created_date": "2024-12-25T14:10:07.069Z",
            "risk_profile": "careful",
            "init_transaction": 0
        }, headers=headers)

        assert response.status_code == 200
        response_json = response.json()
        portfolio_id = response_json["data"]["id"]

        response = requests.post(DELETE_PORTFOLIO, json={"id": portfolio_id}, headers=headers)
        assert response.status_code == 200

    @allure.title("Создание публичного портфеля")
    def test_create_public_portfolio(self):
        headers = {
            "Token": user_token
        }

        response = requests.post(ADD_PORTFOLIO, json={
            "title": "публичный портфель",
            "wallet": "RUB",
            "created_date": "2024-12-25T14:10:07.069Z",
            "risk_profile": "careful",
            "init_transaction": 0,
            "is_public": True
        }, headers=headers)

        assert response.status_code == 200
        response_json = response.json()
        portfolio_id = response_json["data"]["id"]

        response = requests.post(DELETE_PORTFOLIO, json={"id": portfolio_id}, headers=headers)
        assert response.status_code == 200
