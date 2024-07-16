import json
import os.path
from typing import Any

import requests
from dotenv import load_dotenv


def transaction_data(path_file: str) -> list:
    if not os.path.exists(path_file):
        return []
    try:
        with open(path_file, encoding="utf-8") as file:
            data_file = json.load(file)
    except json.JSONDecodeError:
        return []
    if type(data_file) is not list:
        return []
    return data_file


