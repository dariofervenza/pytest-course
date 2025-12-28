# test with expected exceptions: allow an exception that does not make the test to fail


def test_divide_by_zero():
    num = 1 / 0


# solution 1: use try catch, however, pytest provides a construct to handle exceptions --> pytest.raises

import pytest

def test_divide_by_zero_with_raises():
    with pytest.raises(ZeroDivisionError) as e:  # avoid try except
        num = 1 / 0

    # assert that the exception is triggered but inspecting its attributes
    assert "division by zero" in str(e.value)
