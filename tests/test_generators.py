from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

transactions_1 = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]

transactions_2 = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
]

transactions_3 = []


def test_filter_by_currency():
    filter_currency_1 = filter_by_currency(transactions_1, "USD")
    assert next(filter_currency_1) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(filter_currency_1) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert list(filter_by_currency(transactions_2, "USD")) == ["Транзакция в такой валюте отсутствует"]

    assert list(filter_by_currency(transactions_3, "USD")) == ["Пока что никаких транзакций не совершалось"]


def test_transaction_descriptions():
    test_trans_1 = transaction_descriptions(transactions_1)

    assert next(test_trans_1) == "Перевод организации"
    assert next(test_trans_1) == "Перевод со счета на счет"

    test_trans_2 = transaction_descriptions(transactions_2)

    assert next(test_trans_2) == "Перевод организации"

    test_trans_3 = transaction_descriptions(transactions_3)

    assert next(test_trans_3) == ""


def test_card_number_generator():
    get_card_number = card_number_generator(1, 5)
    assert next(get_card_number) == "0000 0000 0000 0001"
    assert next(get_card_number) == "0000 0000 0000 0002"
    assert next(get_card_number) == "0000 0000 0000 0003"
    assert next(get_card_number) == "0000 0000 0000 0004"
    assert next(get_card_number) == "0000 0000 0000 0005"
