import requests
import json
from data import *
from URLS import *



def GetPortfolios(user_token):
    headers = {"Token": user_token}

    response = requests.post(GET_PORTFOLIOS, headers=headers)

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

def GetTransactions(user_token, portfolio_id):
    headers = {"Token": user_token}

    response = requests.post(GET_TRANSACTIONS, headers=headers, json={"portfolio": portfolio_id})

    if response.status_code == 200:
        return response.json()['data']
    else:
        print(f"Ошибка при получении данных для портфеля ID {portfolio_id}")
        return {}


# Функция для сравнения данных портфелей
def compare_portfolio_data(portfolio_data_1, portfolio_data_2):
    # Фильтруем данные по тикерам и операциям (оставляем только те записи, у которых есть тикер и операция)
    data_1 = [
        {
            "operation_name": entry.get("operation_name"),
            "eventPrice": entry.get("eventPrice"),
            "tiker": entry.get("instrument_info", {}).get("tiker"),
            "price": entry.get("price"),
            "currency_code": entry.get("currency_code"),
            "count": entry.get("count", 0)  # Добавляем количество активов (если есть)
        }
        for entry in portfolio_data_1
        if entry.get("instrument_info", {}).get("tiker")  # Фильтруем только те записи, у которых есть тикер
    ]

    data_2 = [
        {
            "operation_name": entry.get("operation_name"),
            "eventPrice": entry.get("eventPrice"),
            "tiker": entry.get("instrument_info", {}).get("tiker"),
            "price": entry.get("price"),
            "currency_code": entry.get("currency_code"),
            "count": entry.get("count", 0)  # Добавляем количество активов (если есть)
        }
        for entry in portfolio_data_2
        if entry.get("instrument_info", {}).get("tiker")  # Фильтруем только те записи, у которых есть тикер
    ]

    # Преобразуем данные в словари, где ключом является тикер, а значением - список операций для этого тикера
    portfolio_dict_1 = {}
    for entry in data_1:
        tiker = entry["tiker"]
        if tiker not in portfolio_dict_1:
            portfolio_dict_1[tiker] = {}
        operation_name = entry["operation_name"]
        if operation_name not in portfolio_dict_1[tiker]:
            portfolio_dict_1[tiker][operation_name] = []
        portfolio_dict_1[tiker][operation_name].append(entry)

    portfolio_dict_2 = {}
    for entry in data_2:
        tiker = entry["tiker"]
        if tiker not in portfolio_dict_2:
            portfolio_dict_2[tiker] = {}
        operation_name = entry["operation_name"]
        if operation_name not in portfolio_dict_2[tiker]:
            portfolio_dict_2[tiker][operation_name] = []
        portfolio_dict_2[tiker][operation_name].append(entry)

    # Сравниваем тикеры: смотрим, какие активы отсутствуют в одном из портфелей
    tickers_1 = set(portfolio_dict_1.keys())  # Тикеры из первого портфеля
    tickers_2 = set(portfolio_dict_2.keys())  # Тикеры из второго портфеля

    missing_in_1 = tickers_2 - tickers_1  # Активы, которых нет в первом портфеле
    missing_in_2 = tickers_1 - tickers_2  # Активы, которых нет во втором портфеле

    if missing_in_1:
        print(f"В первом портфеле отсутствуют следующие активы: {', '.join(missing_in_1)}")
    if missing_in_2:
        print(f"Во втором портфеле отсутствуют следующие активы: {', '.join(missing_in_2)}")

    # Сравниваем операции для одинаковых тикеров в обоих портфелях
    for tiker in tickers_1.intersection(tickers_2):  # Сравниваем только те тикеры, которые есть в обоих портфелях
        print(f"\nСравнение данных для тикера {tiker}:")

        operations_1 = portfolio_dict_1[tiker]
        operations_2 = portfolio_dict_2[tiker]

        # Сравниваем операции для каждого тикера
        for operation_name in set(operations_1.keys()).union(operations_2.keys()):  # Все операции для тикера
            entries_1 = operations_1.get(operation_name, [])
            entries_2 = operations_2.get(operation_name, [])

            # Если операция присутствует в одном портфеле, но отсутствует в другом
            if not entries_1:
                print(f"  Во втором портфеле отсутствует операция '{operation_name}' для тикера {tiker}")
            elif not entries_2:
                print(f"  В первом портфеле отсутствует операция '{operation_name}' для тикера {tiker}")
            else:
                # Сравниваем данные для одинаковых операций
                for entry_1, entry_2 in zip(entries_1, entries_2):
                    for key in entry_1:
                        val_1 = entry_1[key]
                        val_2 = entry_2[key]

                        # Проверка на разницу в значениях
                        if val_1 != val_2:
                            print(f"  Разница в '{key}' для операции '{operation_name}': {val_1} != {val_2}")

                # Сравниваем количество (count) для одинаковых операций
                count_1 = sum(entry["count"] for entry in entries_1)
                count_2 = sum(entry["count"] for entry in entries_2)

                if count_1 != count_2:
                    print(
                        f"  Разница в количестве для операции '{operation_name}' (тикер {tiker}): {count_1} != {count_2}")


def main():

    user_id = int(input('Укажите user_id: '))

    # Получаем список портфелей пользователя
    portfolios = GetPortfolios(user_token)

    if not portfolios:
        print("Портфели не найдены.")
        return

    # Выводим список портфелей
    print("\nСписок портфелей, их айди:")
    for item in portfolios:
        print(f"{item['title']} - {item['id']}")

    # Ввод ID первого портфеля
    portfolio_id_1 = int(input('Укажите ID первого портфеля: '))
    portfolio_data_1 = GetTransactions(user_token, portfolio_id_1)

    if not portfolio_data_1:
        print(f"Ошибка при получении данных для портфеля с ID {portfolio_id_1}.")
        return

    #print(f"\nДанные для портфеля {portfolio_id_1}:")
    #print(json.dumps(portfolio_data_1, indent=2))

    # Ввод ID второго портфеля
    portfolio_id_2 = int(input('Укажите ID второго портфеля для сравнения: '))
    portfolio_data_2 = GetTransactions(user_token, portfolio_id_2)

    if not portfolio_data_2:
        print(f"Ошибка при получении данных для портфеля с ID {portfolio_id_2}.")
        return

    #print(f"\nДанные для портфеля {portfolio_id_2}:")
    #print(json.dumps(portfolio_data_2, indent=2))

    # Сравниваем данные
    compare_portfolio_data(portfolio_data_1, portfolio_data_2)


if __name__ == "__main__":
    main()