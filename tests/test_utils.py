from unittest.mock import mock_open, patch

import pytest

from src.utils import transaction_data
from src.external_api import get_transaction_amount_in_rub


def test_file_not_exists():
    result = transaction_data("fake_path.json")
    assert result == []


@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open)
def test_invalid_json(mock_open, mock_exists):
    mock_exists.return_value = True
    mock_open.return_value.read.return_value = "{invalid_json}"
    assert transaction_data("invalid.json") == []


@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open)
def test_not_a_list(mock_open, mock_exists):
    mock_exists.return_value = True
    mock_open.return_value.read.return_value = '{"key": "value"}'
    assert transaction_data("not_a_list.json") == []


@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open)
def test_valid_json(mock_open, mock_exists):
    mock_exists.return_value = True
    mock_open.return_value.read.return_value = '[{"transaction": 1}, {"transaction": 2}]'
    assert transaction_data("valid.json") == [{"transaction": 1}, {"transaction": 2}]


@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open)
def test_empty_list(mock_open, mock_exists):
    mock_exists.return_value = True
    mock_open.return_value.read.return_value = "[]"
    assert transaction_data("empty_list.json") == []


def test_amount_in_rub():
    """Тестирует случай, когда валюта уже в RUB"""
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    result = get_transaction_amount_in_rub(transaction)
    assert result == 31957.58


@patch("requests.get")
def test_amount_in_usd(mock_get):
    """Тестирует случай, когда валюта в USD и требуется конвертация"""
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    mock_response = {"success": True, "result": 727008.19}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response
    result = get_transaction_amount_in_rub(transaction)
    assert result == 727008.19


@patch("requests.get")
def test_amount_convert_error(mock_get):
    transaction = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    mock_response = {"success": False}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response
    with pytest.raises(ValueError) as exc_info:
        get_transaction_amount_in_rub(transaction)
    assert str(exc_info) == ("<ExceptionInfo ValueError('Неудалось получить обменный курс из USD в RUB') " "tblen=2>")
