import json
import logging
import os.path

logger = logging.getLogger("utils")
logger.setLevel(logging.CRITICAL)
file_handler = logging.FileHandler("..\\logs\\utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transaction_data(path_file: str) -> list:
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях. Если файл
    пустой, содержит не список или не найден, функция возвращает пустой список."""
    if not os.path.exists(path_file):
        logger.critical(f"Файла {path_file} не существует")
        return []
    try:
        logger.info("Считываем содержимое файла")
        with open(path_file, encoding="utf-8") as file:
            data_file = json.load(file)
    except json.JSONDecodeError as ex:
        logging.error(f"Произошла ошибка: {ex}")
        return []
    if type(data_file) is not list:
        logger.critical(f"Файл {path_file} не содержит список")
        return []
    return data_file
