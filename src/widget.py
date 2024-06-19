from src.masks import get_mask_account, get_mask_card_number
def mask_account_card(card_name_mask: str) -> str:
    """Функция возвращающая названия и маску карты"""
    name_mask = card_name_mask.split(" ")
    if len(name_mask[1]) == 16:
        return f"{name_mask[0]} {get_mask_card_number(name_mask[1])}"
    elif len(name_mask[1]) == 20:
        return f"{name_mask[0]} {get_mask_account(name_mask[1])}"
    else:
        return "Неверный формат"


def get_data(data_time: str) -> str:
    parts = data_time.split("T")
    data = parts[0]
    format_data = data[8:] + "." + data[5:7] + "." + data[:4]
    return format_data


