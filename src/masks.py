import logging
from typing import Union

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("..\\logs\\masks.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: Union[int, str]) -> str:
    """Функция которая возвращает маску номера карты"""
    convert_number_card = str(number_card)
    if len(convert_number_card) != 16:
        return "Неверный формат номера карты"
    else:
        logger.info("Составляем маску карты")
        mask_card = (
            convert_number_card[:4]
            + " "
            + convert_number_card[4:6]
            + "**"
            + " "
            + "****"
            + " "
            + convert_number_card[12:]
        )
        return mask_card


def get_mask_account(number_check: Union[int, str]) -> str:
    """Функция которая возращает маску номера счета"""
    logger.info("Составляем маску счета")
    convert_number_check = str(number_check)
    if len(convert_number_check) != 20:
        return "Неверный формат номера счета"
    else:
        mask_account = "**" + convert_number_check[-4:]
        return mask_account
