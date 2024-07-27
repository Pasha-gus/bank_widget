from src.filters import count_operations_by_category, filter_by_line


# Тесты для функции filter_by_line
def test_filter_by_line():
    operations = [
        {"description": "Оплата интернет-магазина", "amount": 100, "date": "2023-10-01"},
        {"description": "Перевод на счет", "amount": 200, "date": "2023-10-02"},
        {"description": "Кредитный платеж", "amount": 300, "date": "2023-10-03"},
    ]

    # Проверяем фильтрацию по слову "интернет"
    result = filter_by_line(operations, "интернет")
    assert len(result) == 1
    assert result[0]["description"] == "Оплата интернет-магазина"

    # Проверяем фильтрацию по слову "платеж"
    result = filter_by_line(operations, "платеж")
    assert len(result) == 1
    assert result[0]["description"] == "Кредитный платеж"

    # Проверяем, что ничего не найдено
    result = filter_by_line(operations, "покупка")
    assert len(result) == 0


# Тесты для функции count_operations_by_category
def test_count_operations_by_category():
    operations = [
        {"description": "Покупка в магазине", "amount": 100, "date": "2023-10-01"},
        {"description": "Оплата кредита", "amount": 200, "date": "2023-10-02"},
        {"description": "Доставка товаров", "amount": 300, "date": "2023-10-03"},
        {"description": "Покупка в магазине", "amount": 400, "date": "2023-10-04"},
    ]

    categories = ["Покупка в магазине", "Оплата кредита", "Доставка товаров"]

    count = count_operations_by_category(operations, categories)

    assert count["Покупка в магазине"] == 2
    assert count["Оплата кредита"] == 1
    assert count["Доставка товаров"] == 1

    # Проверка на пустой список операций
    empty_count = count_operations_by_category([], categories)
    assert empty_count["Покупка в магазине"] == 0
    assert empty_count["Оплата кредита"] == 0
    assert empty_count["Доставка товаров"] == 0

    # Проверка на категории, которых нет в операциях
    new_count = count_operations_by_category(operations, ["Неизвестная категория"])
    assert new_count["Неизвестная категория"] == 0
