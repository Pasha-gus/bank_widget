import os.path

from src.filters import filter_by_line
from src.processing import filter_by_state, sort_by_date
from src.utils import transaction_data, transaction_data_csv, transaction_data_excel
from src.widget import get_data, mask_account_card


def main():
    print(
        """Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )

    menu_items = input("Введите пункт (1, 2 или 3): ")

    while menu_items not in ["1", "2", "3"]:
        print("Вы ввели неоректный символ, поробуйте ещё раз")
        menu_items = input("Введите пункт (1, 2 или 3): ")

    if menu_items == "1":
        print("Для обработки выбран JSON-файл")
        file_used_data = transaction_data(path_json)
    elif menu_items == "2":
        print("Для обработки выбран CSV-файл")
        file_used_data = transaction_data_csv(path_csv)
    elif menu_items == "3":
        print("Для обработки выбран XLSX-файл")
        file_used_data = transaction_data_excel(path_xlsx)
    print(
        """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
    )
    sort_status = input()
    while sort_status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции {sort_status} недоступен.")
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
        """
        )
        sort_status = input()
    sort_status_data = filter_by_state(file_used_data)
    print("Отсортировать операции по дате?\n")
    sort_by_date_input = input("(Да/Нет):")
    while sort_by_date_input.lower() not in ["да", "нет"]:
        print("Некоректно дан ответ на вопрос\n")
        print("Отсортировать операции по дате?\n")
        sort_by_date_input = input("(Да/Нет):")
    if sort_by_date_input == "да":
        sort_date = True
        print("Отсортировать по возрастанию или по убыванию\n")
        sort_by_age_input = input("(по возрастанию/по убыванию): ")
        while sort_by_age_input.lower() not in ["по возрастанию", "по убыванию"]:
            print("Некоректно дан ответ на вопрос\n")
            print("Отсортировать по возрастанию или по убыванию\n")
            sort_by_age_input = input("(по возрастанию/по убыванию): ")
        if sort_by_age_input.lower() == "по убыванию":
            sort_age = True
        else:
            sort_age = False
    else:
        sort_date = False
    print("Выводить только рублевые транзакции")
    rub_tran_input = input("(Да/Нет):")
    while rub_tran_input.lower() not in ["да", "нет"]:
        print("Некоректно дан ответ на вопрос\n")
        print("Выводить только рублевые транзакции")
        rub_tran_input = input("(Да/Нет):")
    if rub_tran_input.lower() == "да":
        rub_tran = True
    else:
        rub_tran = False
    print("Отфильтровать список транзакций по определенному слову в описании")
    filter_description_input = input(
        "(Если да то впишите слово по которому нужно отфильтровать, если нет напишите 'нет'):"
    )
    if filter_description_input.lower() == "нет":
        filter_description = False
    else:
        filter_description = filter_description_input
    print("Распечатываю итоговый список транзакций...")
    if sort_date:
        list_sort_data = sort_by_date(sort_status_data, sort_age)
    else:
        list_sort_data = sort_status_data
    if rub_tran:
        rub_tran_list = [tran for tran in list_sort_data if tran["currency_code"] == "RUB"]
    else:
        rub_tran_list = list_sort_data
    if filter_description:
        finaly_list = filter_by_line(rub_tran_list, filter_description)
    else:
        finaly_list = rub_tran_list
    if finaly_list:
        print(finaly_list)
        print(f"Всего банковских операций в выборке: {len(finaly_list)}\n")
        for transaction in finaly_list:
            if "from" in transaction:
                if not transaction["from"] or type(transaction["from"]) == float:
                    print(
                        f"""{get_data(transaction["date"])} {transaction["description"]}
{mask_account_card(transaction["to"])}
Сумма: {transaction["amount"]} {transaction["currency_name"]}\n"""
                    )
                elif not transaction["to"] or type(transaction["to"]) == float:
                    print(
                        f"""{get_data(transaction["date"])} {transaction["description"]}
{mask_account_card(transaction["from"])}
Сумма: {transaction["amount"]} {transaction["currency_name"]}\n"""
                    )
                else:
                    print(
                        f"""{get_data(transaction["date"])} {transaction["description"]}
{mask_account_card(transaction["from"])} -> {mask_account_card(transaction["to"])}
Сумма: {transaction["amount"]} {transaction["currency_name"]}\n"""
                    )
            else:
                print(
                    f"""{get_data(transaction["date"])} {transaction["description"]}
{mask_account_card(transaction["to"])}
Сумма: {transaction["amount"]} {transaction["currency_name"]}\n"""
                )
    else:
        print(
            """Не найдено ни одной транзакции, подходящей под ваши
условия фильтрации"""
        )


if __name__ == "__main__":
    path_json = os.path.join(os.path.dirname(__file__), "data", "operations.json")
    path_csv = os.path.join(os.path.dirname(__file__), "data", "transactions.csv")
    path_xlsx = os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")
    main()
