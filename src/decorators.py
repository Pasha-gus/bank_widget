from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования вызова функции.
    Логирует успешные файлы или ошибки в текстовый файл или консоль
    Args:
        filename (str, optional): Имя файла для логирования. Если не указано, логирование происходит в консоль.

    Returns:
        function: Обёрнутая функция с логированием.

    """

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            log_message = ""
            try:
                result = function(*args, **kwargs)
                log_message += f"{function.__name__}: ok"
                return result
            except Exception as e:
                log_message += f"{function.__name__} error: {str(e)}. Inputs: {args}, {kwargs}"
                raise e
            finally:
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(log_message)
                else:
                    print(log_message)

        return wrapper

    return decorator
