import pytest

from src.decorators import log


@log()
def function_1(x, y):
    return x + y


@log()
def function_2(x, y):
    return x / y


def test_function_1_success(capsys):
    result = function_1(1, 2)
    assert result == 3

    captured = capsys.readouterr()
    assert captured.out == "function_1: ok\n"


def test_function_2_exception(capsys):
    with pytest.raises(ZeroDivisionError):
        function_2(1, 0)

    captured = capsys.readouterr()
    assert captured.out == "function_2 error: division by zero. Inputs: (1, 0), {}\n"
