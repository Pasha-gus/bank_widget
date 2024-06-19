from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_data

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