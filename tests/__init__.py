from example import add_function
from nose.tools import assert_equals


def test_add_zero_to_number():
    number = 5
    result = add_function(0, number)

    assert_equals(number, result)
