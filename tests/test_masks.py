from src.masks import get_mask_account, get_mask_card_number


def test_mask_card():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("1327819213124") == "Неверный формат номера карты"
    assert get_mask_card_number("") == "Неверный формат номера карты"


def test_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("1234122132412") == "Неверный формат номера счета"
    assert get_mask_account("") == "Неверный формат номера счета"
