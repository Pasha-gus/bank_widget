def filter_by_state(list_of_dicts: list, state="EXECUTED") -> list:
    """Ищет среди списка словарей, словарь у которого значение ключа state совпадает со значением
    переданным в функцию"""
    filtered_list = [d for d in list_of_dicts if d.get("state") == state]
    return filtered_list


def sort_by_date(list_of_dicts: list, order=True) -> list:
    """Функция которая сортирует словари по дате в порядке убывания или возрастания"""
    sorted_list = sorted(list_of_dicts, key=lambda x: x["date"], reverse=(order is True))
    return sorted_list
