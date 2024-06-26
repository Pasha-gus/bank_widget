from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_name_mask: str) -> str:
    """Функция возвращающая названия и маску карты"""
    name_mask = card_name_mask.split(" ")
    if name_mask[0] == "Счет":
        if len(name_mask[1]) == 20:
            return f"{name_mask[0]} {get_mask_account(name_mask[1])}"
        else:
            return "Неверный формат номера счета"
    elif len(name_mask) == 2:
        if len(name_mask[-1]) == 16:
            return f"{name_mask[0]} {get_mask_card_number(name_mask[1])}"
        else:
            return "Неверный формат номера карты"
    elif len(name_mask) == 3:
        if len(name_mask[-1]) == 16:
            return f"{" ".join(name_mask[0:2])} {get_mask_card_number(name_mask[2])}"
        else:
            return "Неверный формат номера карты"
    else:
        mask = "".join(name_mask[-4:])
        if len(mask) == 16:
            return f"{" ".join(name_mask[0:-4])} {get_mask_card_number(mask)}"
        else:
            return "Неверный формат номера карты"


def get_data(data_time: str) -> str:
    if "T" in data_time:
        parts = data_time.split("T")
        data = parts[0]
        format_data = data[8:] + "." + data[5:7] + "." + data[:4]
        return format_data
    else:
        raise ValueError("Неправильно задан формат даты")
