from unittest.mock import Mock, mock_open, patch

from src.utils import transaction_data, transaction_data_csv, transaction_data_excel



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
def test_empty_list(mock_open, mock_exists):
    mock_exists.return_value = True
    mock_open.return_value.read.return_value = "[]"
    assert transaction_data("empty_list.json") == []


def test_file_csv_not_exist():
    result = transaction_data_csv("fake_path")
    assert result == []


def test_transaction_data_csv_success():
    mock_file_content = "id;state;date;amount;currency_name;currency_code;from;to;description\n650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n"

    with patch("builtins.open", mock_open(read_data=mock_file_content)):
        result = transaction_data_csv("mocked_path.csv")

    expected_result = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]

    assert result == expected_result


def test_transaction_data_excel_success():
    mock_data = Mock()
    mock_data.to_dict.return_value = [{"column1": "value1", "column2": "value2"}]

    with patch("pandas.read_excel", return_value=mock_data):
        result = transaction_data_excel("dummy_path.xlsx")

        assert result == [{"column1": "value1", "column2": "value2"}]


def test_transaction_data_excel_file_not_found():
    with patch("pandas.read_excel", side_effect=FileNotFoundError):
        result = transaction_data_excel("dummy_path.xlsx")

        assert result == []


def test_transaction_data_excel_value_error():
    with patch("pandas.read_excel", side_effect=ValueError("Invalid format")):
        result = transaction_data_excel("dummy_path.xlsx")

        assert result == []


def test_transaction_data_excel_other_exception():
    with patch("pandas.read_excel", side_effect=Exception("Some other error")):
        result = transaction_data_excel("dummy_path.xlsx")

        assert result == []
