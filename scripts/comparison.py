import requests
porfolioId = 20202
token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzY5NTYyOTEsInN1YiI6IndlYiIsImFjYyI6eyJleHQiOjEsImJvb2siOjEsImNsdWIiOjEsIm1wMy4xIjoxLCJyZWZfYSI6MSwiY2x1Yl9wIjoxLCJlbXBsb3llZSI6MX0sIlUiOjI4MTY3LCJTIjoyNDEwMjU3MywianRpIjoiMjUwODk3MDQiLCJsYW5nIjoiUlUiLCJpYXQiOjE3MzY5NTI2OTEsInVwZGF0ZSI6IjIwMjItMTAtMjYgMTM6NDg6MTYuOTEyNDU4KzAzOjAwIiwiZnAiOiIiLCJ0YXJpZmYiOlt7InQiOjEwMDI4LCJwIjpbMTZdLCJmIjoyfSx7InQiOjEwMDI4LCJwIjpbMTZdLCJmIjo3fSx7InQiOjEwMDYwLCJwIjpbMTZdfSx7InQiOjEwMDYyLCJwIjpbMTddfSx7InQiOjEwMDYzLCJwIjpbMTddfSx7InQiOjEwMDY0LCJwIjpbMTddfSx7InQiOjEwMDkyLCJwIjpbNzMsNzQsNzUsNzcsNzksMTQsODIsNzFdfV19.RoqUdjjJKlOhTdx6vYy76kcWS1lFd05UAHNP9D7EhhlnfPA41KQlIFoToRsmh4zy8LNHTqhFPkhQgncU-xDtvVOksulpwsT6pfuytXxDbgeSwYBLY0vM4vMAzdyKHrlx0QbUyp54cFi7r-z6k7Rcyr-zRKp215asyrFWBDc_CZmroPzW7whkvhKgCAEbDckLnorPioySOH1zAONTO7ZREumjI0t34oGl6FyydNj1rL66qIop6s1gbKfmilsXT7H0Dmy_jpuCTc792PUXjROhEDGMHsHFrrXYDJZUvHDMP6eTLPGKrsD8obfm9mjJCiDB69YAr2uCCay3TaJGHn1eFQ'
def getPortfolioAnalytics():
    url = 'https://test.profinansy.ru/api/portfolios/getPortfolioAnalytics'  # Убедитесь, что URL указан правильно

    headers = {
        "Token": token  # Убедитесь, что переменная `token` правильно установлена
    }

    data = {
        "id": porfolioId  # Убедитесь, что переменная `porfolioId` правильно установлена
    }

    # Отправляем POST-запрос и получаем ответ
    response = requests.post(url, headers=headers, json=data)

    # Выводим статус код ответа для диагностики
    print(f"Response status code: {response.status_code}")

    # Проверяем, что запрос прошел успешно
    if response.status_code == 200:
        # Получаем данные из ответа
        response_data = response.json()
        print("Response data:", response_data)
    else:
        print(f"Request failed with status code: {response.status_code}")
def getPortfolioAnalytics2():
    url = 'https://test.profinansy.ru/api/portfolios/getPortfolioAnalytics'

    headers = {
        "Token": token
    }

    data = {
        "id": porfolioId
    }

    # Отправляем POST-запрос и получаем ответ
    response = requests.post(url, headers=headers, json=data)

    # Проверяем, что запрос прошел успешно
    if response.status_code == 200:
        # Получаем данные из ответа
        response_data = response.json()
        print("Response data:", response_data)

        # Проводим проверку на правильность значений
        if response_data['data']['prices']['amount'] == 4210 and response_data['data']['prices']['data']['stock'][
            'amount'] == 4210:
            print("Amount is correct")
        else:
            print("Amount is incorrect")
    else:
        print(f"Request failed with status code: {response.status_code}")