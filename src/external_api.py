import os.path
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def get_transaction_amount_in_rub(transaction: dict[str, Any]) -> float:
    """принимает на вход транзакцию и возвращает сумму транзакции в рублях,
    . Если транзакция была в
    USD
     или
    EUR
    , происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли"""
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency == "RUB":
        return amount
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("success") and "result" in data:
                return float(data["result"])
            raise ValueError(f"Неудалось получить обменный курс из {currency} в RUB")
