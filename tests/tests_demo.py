from src.masks import get_mask_account, get_mask_card_number

number_card = 7000792289606361
number_check = 73654108430135874305
print(f"Маска номера карты: {get_mask_card_number(number_card)}")
print(f"Маска номера счета: {get_mask_account(number_check)}")
