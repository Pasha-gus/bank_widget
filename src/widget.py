import masks
def mask_account_card(card_name_mask: str) -> str:
    name_mask = card_name_mask.split()
    if len(name_mask[1]) == 16:
        return f"{name_mask[0]} {masks.get_mask_card_number(name_mask[1])}"
    elif len(name_mask[1]) == 20:
        return f"{name_mask[0]} {masks.get_mask_account(name_mask[1])}"
    else:
        return "Неверный формат"

