import re


def filter_by_line(operations: list[dict], search_line: str) -> list[dict]:
    """принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список словарей,
    у которых в описании есть данная строка."""
    pattern = re.compile(search_line, re.IGNORECASE)
    result_operations = [
        operation
        for operation in operations
        if "description" in operation and pattern.search(operation["description"])
    ]
    return result_operations


def count_operations_by_category(operations: list[dict], categories: list[str]) -> dict[str, int]:
    """принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    category_count = {category: 0 for category in categories}

    for operation in operations:
        if "description" in operation:
            for category in categories:
                if category.lower() in operation["description"].lower():
                    category_count[category] += 1

    return category_count
