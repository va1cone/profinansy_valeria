import requests
import json


def GetPositions():
    url = 'https://invest-public-api.tinkoff.ru/rest/tinkoff.public.invest.api.contract.v1.OperationsService/GetPositions'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    data = {
        "accountId": accountId
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response = response.json()

        return response

    return None


def FindInstrument(figi):
    url = 'https://invest-public-api.tinkoff.ru/rest/tinkoff.public.invest.api.contract.v1.InstrumentsService/FindInstrument'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    data = {
        "query": figi
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response = response.json()

        instruments = response['instruments']

        codes = []

        for item in instruments:
            isin = item['isin']
            ticker = item['ticker']
            if isin not in codes:
                codes.append(isin)
            if ticker not in codes:
                codes.append(ticker)

        return codes

    return None


def GetAccounts():
    url = 'https://invest-public-api.tinkoff.ru/rest/tinkoff.public.invest.api.contract.v1.UsersService/GetAccounts'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    data = {
        "status": "ACCOUNT_STATUS_UNSPECIFIED"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response = response.json()

        accounts = response['accounts']

        accounts_list = []

        for item in accounts:
            id = item['id']
            name = item['name']
            accounts_list.append({"id": id, "name": name})

        return accounts_list

    return None


def GetToken(user_id):
    url = 'https://profinansy.ru/api/auth/adm/adm_login'

    headers = {
        "Token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzI2MjYzOTEsInN1YiI6IndlYiIsImFjYyI6eyJBRE0iOjEsIk1PRCI6MSwiZXh0IjoxLCJpcG8iOjEsInJlcCI6MSwiYm9vayI6MSwiY2x1YiI6MSwiaWRlYSI6MSwiY2x1Yl9wIjoxLCJNT0RfaW5zIjoxLCJsbXNfYWRtIjoxLCJsbXNfZXhwIjoxLCJBRE1fdXNlciI6MSwiTU9EX2RpY3QiOjEsIk1PRF9uZXdzIjoxLCJBRE1fbG9naW4iOjEsInRnX2NoYW5uZWwiOjF9LCJVIjo0NDMwMDI0LCJTIjoxMDQ0NzQ2MywianRpIjoxNjM2OTE3NzIsImxhbmciOiJSVSIsImlhdCI6MTczMjYyMjc5MSwidXBkYXRlIjoiMjAyMi0xMC0yNiAxMzo0ODoxNi45MTI0NTgrMDM6MDAiLCJmcCI6IiIsInRhcmlmZiI6W3sidCI6OTAwMSwicCI6WzEyOF19LHsidCI6MTAwMjYsInAiOls5XX0seyJ0IjoxMDAyOCwicCI6WzE2XSwiZiI6N30seyJ0IjoxMDAzOCwicCI6WzIwXX0seyJ0IjoxMDAzOSwicCI6WzNdfSx7InQiOjEwMDQzLCJwIjpbOF19LHsidCI6MTAwNDcsInAiOls0OSw1OCwxMDFdfSx7InQiOjEwMDUwLCJwIjpbMTksMzAsMzFdfSx7InQiOjEwMDY1LCJwIjpbNDVdfSx7InQiOjEwMDc4LCJwIjpbNTRdLCJmIjo0fSx7InQiOjEwMDc4LCJwIjpbNTRdLCJmIjo5fSx7InQiOjEwMDg2LCJwIjpbNjNdfSx7InQiOjEwMDkxLCJwIjpbNzFdfSx7InQiOjEwMDkyLCJwIjpbNzEsNzMsNzQsNzUsNzcsNzgsNzksODEsODcsODgsNjUsOTMsOTQsOTgsMTA3LDEwOSwxMTAsMTE1LDExNiwxMTgsMTIxLDEyNCwxMjksMTMwLDEzMywxMzUsMTM2LDEzNywxMzksMTgwLDE4MSwxODIsMTcyLDE4MywxODQsMTg1LDE4OCwxOTEsMTkyLDE5OSwyMDIsMjAzLDE3MywyNDAsMjQzLDI1MSwyNTIsMjUzLDI1NF19LHsidCI6MTAwOTgsInAiOlsxNzVdfSx7InQiOjEwMTU2LCJwIjpbMTIwXX0seyJ0IjoxMDI2NiwicCI6WzE4N119LHsidCI6MTAxMDUsInAiOls4NV19LHsidCI6MTAxMDYsInAiOls4NF19LHsidCI6MTAxMjMsInAiOls5Nl19XX0.c4mMUEXWRXtI4WxlhbJpCi6wiQyameCQe7qRJxlJRlVU7zrDvB1MGQo0Zs35sHsyVidYWG4-yqLLKIel-pxuT9uGDkhdcl86A_JyVEgrQTEifeLrlgXLbfJOY7tMDurpsBbQNb7EqJ_Yz5yhnhGW8gyl_S2QvOWwpW3yPWbK2pIDglvMKQFvLb9Jqan711KmOSDtTk708bOOppJZFNpfVBH14JKvwBLHpRYoamc1UP-gCFXuQxVzXlY2nn-utOSzqxJ1ch5_ISQYhIRHaBYAy9N-1zPGM_X0qhNhp76L9Ix6N-_QjBM9UXnvee9dbA0-U9_udd9-HNJN7rRfSbR1tw"
    }

    data = {
        "user_id": user_id
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response = response.json()
        login = response['login']
        password = response['password']
    else:
        return None

    url = 'https://profinansy.ru/api/auth/session?type=web'

    response = requests.get(url)

    if response.status_code == 200:
        response = response.json()
        anon_token = response['token']
    else:
        return None

    url = 'https://profinansy.ru/api/auth/login'

    headers = {
        "Token": anon_token
    }

    data = {
        "login": login,
        "acc_type": "email",
        "pass": password,
        "web": True
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response = response.json()
        user_token = response['token']

        return user_token
    else:
        return None


def GetPortfolios(user_token):
    url = 'https://profinansy.ru/api/portfolios/getPortfolios'

    headers = {
        "Token": user_token
    }

    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        response = response.json()
        data = response['data']

        portfolios = []

        for item in data:
            id = item['id']
            title = item['title']
            portfolios.append({"id": id, "title": title})

        return portfolios

    return None


def GetAssetInfo(user_token, porfolioId):
    url = 'https://profinansy.ru/api/portfolios/getPortfolioAssetsInfo'

    headers = {
        "Token": user_token
    }

    data = {
        "id": porfolioId
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response = response.json()

        result = []
        for category in response['data']['result']:
            if 'data' in response['data']['result'][category]:
                items = response['data']['result'][category]['data']
                for item in items:
                    if 'instrument_info' in item and 'count' in item and item['count'] > 0:
                        code = item['instrument_info'].get('code', 'N/A')
                        code = code.replace('-MOEX', '')
                        code = code.replace('-NYSE', '')
                        code = code.replace('-NASDAQ', '')
                        result.append({
                            "code": code,
                            "count": item.get('count', 0)
                        })

        return result

    return None


def compare_pf_and_broker(pf, broker):
    pf_mapping = {entry['code']: entry['count'] for entry in pf}

    discrepancies = []
    for broker_entry in broker:
        broker_codes = broker_entry['code']
        broker_count = int(broker_entry['count'])

        matching_codes = [code for code in broker_codes if code in pf_mapping]

        if matching_codes:
            for code in matching_codes:
                if pf_mapping[code] != broker_count:
                    discrepancies.append({
                        "code": code,
                        "expected_count": broker_count,
                        "actual_count": pf_mapping[code]
                    })
        else:
            discrepancies.append({
                "code": broker_codes,
                "expected_count": broker_count,
                "actual_count": None
            })

    return discrepancies


###

user_id = int(input('Укажите user_id: '))
user_token = GetToken(user_id)

for item in GetPortfolios(user_token):
    print(f'{item['title']} - {item['id']}')

porfolioId = int(input('Укажите ID портфеля: '))
PfPorfolioAsset = GetAssetInfo(user_token, porfolioId)
print(PfPorfolioAsset)

token = str(input('Укажите токен брокера: '))

for item in GetAccounts():
    print(f'{item['name']} - {item['id']}')

accountId = int(input('Укажите ID счета: '))

data = GetPositions()

# money = data['money']

# print('Свободные деньги:')
# for item in money:
#     currency = item['currency']
#     value = int(item['units']) + int(item['nano'])/1000000000
#     if value == 0:
#         continue
#     print(f'Валюта: {currency}, остаток: {value}')

# print()

securities = data['securities']

BrokerPortfolioAsset = []
for item in securities:
    figi = item['figi']
    instrument = FindInstrument(figi)
    balance = item['balance']
    BrokerPortfolioAsset.append({"code": instrument, "count": balance})

print(BrokerPortfolioAsset)

print()

print(compare_pf_and_broker(PfPorfolioAsset, BrokerPortfolioAsset))