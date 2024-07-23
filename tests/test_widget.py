import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    "number_card_account, musk_card_account",
    [
        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1231234123", "Неверный формат номера карты"),
        ("Счет 142131", "Неверный формат номера счета"),
        ("", "Неверный формат номера карты"),
    ],
)
def test_mask_account_card(number_card_account, musk_card_account):
    assert mask_account_card(number_card_account) == musk_card_account


def test_get_data(data_time):
    assert get_data(data_time) == "11.07.2018"

    with pytest.raises(ValueError) as exc_info:
        get_data("12.01.23")

    assert str(exc_info.value) == "Неправильно задан формат даты"
