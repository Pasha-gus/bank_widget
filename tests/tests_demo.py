from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_data, mask_account_card
from src.processing import filter_by_state, sort_by_date

number_card = 7000792289606361
number_check = 73654108430135874305
name_number_card = "Maestro 1596837868705199"
name_number_check = "Счет 64686473678894779589"
data = "2018-07-11T02:26:18.671407"
print(f"Маска номера карты: {get_mask_card_number(number_card)}")
print(f"Маска номера счета: {get_mask_account(number_check)}")
print(f"Маска номера карты: {mask_account_card(name_number_card)}")
print(f"Маска номера счета: {mask_account_card(name_number_check)}")
print(f"Дата: {get_data(data)}")

sorted_list_desc = filter_by_state(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
)

print(sorted_list_desc)

sorted_list_desc = sort_by_date(
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
)

print(sorted_list_desc)