import csv
import json
import logging
import os.path

import pandas as pd

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
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


def transaction_data_csv(path_file: str) -> list:
    """Принимает на вход путь до CSV-файла и возвращает список словарей с данными о финансовых транзакциях."""
    data_file = []
    try:
        logger.info("Считываем содержимое файла")
        with open(path_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                data_file.append(row)
        return data_file

    except FileNotFoundError:
        logger.error(f"Ошибка: файл {path_file} не существует")
        return []
    except csv.Error as csv_err:
        logger.error(f"Ошибка при считывании файла CSV: {csv_err}")
        return []
    except Exception as ex:
        logger.error(f"Ошибка при считывании файла: {ex}")
        return []


def transaction_data_excel(path_file: str) -> list:
    try:
        logger.info(f"Считываем содержимое файла {path_file}")
        excel_data = pd.read_excel(path_file)
        transaction_list = excel_data.to_dict(orient="records")
        return transaction_list
    except FileNotFoundError:
        logger.error(f"Ошибка: Файл {path_file} не найден")
        return []
    except ValueError as ex:
        logger.error(f"Ошибка: {ex} неправильный формат файла")
        return []
    except Exception as ex:
        logger.error(f"Ошибка: {ex}")
        return []
