import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_data, mask_account_card


def test_mask_card():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("1327819213124") == "Неверный формат номера карты"
    assert get_mask_card_number("") == "Неверный формат номера карты"


def test_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("1234122132412") == "Неверный формат номера счета"
    assert get_mask_account("") == "Неверный формат номера счета"


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


def test_filter_by_state(list_desc):
    assert filter_by_state(list_desc, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(list_desc, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    assert filter_by_state(list_desc) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date(list_desc) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date(list_desc, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
