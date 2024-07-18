from unittest.mock import mock_open, patch

from src.utils import transaction_data


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
