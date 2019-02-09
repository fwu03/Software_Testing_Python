# test_flatten_list_prime.py

import pytest
import mlist

def test_format():
    with pytest.raise(TypeError):
        mlist.flatten_list_prime([["hello"], [3,5]])  # return ERROR if input contain strings
        mlist.flatten_list_prime({"1": "what",
                         "2": "5",
                         "hello": "6"})  # return ERROR if input is not a list (eg. dictionary)


def test_values():
    with pytest.raise(TypeError):
        mlist.flatten_list_prime([[-5], [3,5550]])  # return ERROR if input contains values over 1000
        mlist.flatten_list_prime([[-5], [3.0,15]])  # return ERROR if input contains float

def test_output():
    assert mlist.flatten_list_prime([[12,5], [2,3]]) == [3,5] # assert return contain correct values
    assert type(mlist.flatten_list_prime([[12,5], [2,3]])) == "list" # assert return is a list
    assert length(mlist.flatten_list_prime([[12,5], [2,3]])) >= length([[12,5], [2,3]])  # assert return length is less than or equal to input length
