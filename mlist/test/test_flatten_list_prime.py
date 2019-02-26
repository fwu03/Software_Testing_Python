# test_flatten_list_prime.py

import pytest
from mlist import flatten_list_prime

def test_format():
    with pytest.raises(TypeError):
        flatten_list_prime.flatten_list_prime([["hello"], [3, 5]])  # return ERROR if input contain strings
        flatten_list_prime.flatten_list_prime({"1": "what",
                         "2": "5",
                         "hello": "6"})  # return ERROR if input is not a list (eg. dictionary)
        flatten_list_prime.flatten_list_prime([[-5], [3.0, 15]])  # return ERROR if input contains float


def test_values():
    with pytest.raises(ValueError):
        flatten_list_prime.flatten_list_prime([[-5], [3, 5550]])  # return ERROR if input contains values over 1000

def test_output():
    assert flatten_list_prime.flatten_list_prime([[12, 5], [2, 3]]) == [2, 3, 5], "list not flattening" # assert return contain correct values
    assert isinstance(flatten_list_prime.flatten_list_prime([[12, 5], [2, 3]]), list), "output not a list" # assert return is a list
    assert len(flatten_list_prime.flatten_list_prime([[12, 5], [2, 3]])) >= len([[12, 5], [2, 3]]), "length of output should not be greater than length of input"  # assert return length is less than or equal to input length
