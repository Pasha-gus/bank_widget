def filter_by_currency(transactions: list, currency: str):
    """Функция фильтрует транзакции по валюте и возвращает итератор."""
    if not transactions:
        yield "Пока что никаких транзакций не совершалось"
    else:
        has_currency = False
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["name"] == currency:
                has_currency = True
                yield transaction
        if not has_currency:
            yield "Транзакция в такой валюте отсутствует"


def transaction_descriptions(transactions: list):
    """Функция принимает на вход список словарей транзакций и возращает описание каждой операции по очереди"""
    if not transactions:
        yield ""
    else:
        for transaction in transactions:
            yield transaction.get("description", "")


def card_number_generator(start: int, end: int):
    current = start
    while current <= end:
        long_current = len(str(current))
        card_number = ""
        while len(card_number) < 16 - long_current:
            card_number += "0"
        card_number += str(current)
        format_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
        yield format_card_number
        current += 1
