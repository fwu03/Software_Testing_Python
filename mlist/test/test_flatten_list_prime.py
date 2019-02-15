# test_flatten_list_prime.py

import pytest
import mlist

def test_format():
    with pytest.raises(TypeError("Input must be list of intergers")):
        mlist.flatten_list_prime([["hello"], [3, 5]])  # return ERROR if input contain strings
        mlist.flatten_list_prime({"1": "what",
                         "2": "5",
                         "hello": "6"})  # return ERROR if input is not a list (eg. dictionary)
        mlist.flatten_list_prime([[-5], [3.0, 15]])  # return ERROR if input contains float


def test_values():
    with pytest.raises(ValueError("Input values exceed 1000. Please limit range of input values to less than 1000.")):
        mlist.flatten_list_prime([[-5], [3, 5550]])  # return ERROR if input contains values over 1000

def test_output():
    assert mlist.flatten_list_prime.flatten_list_prime([[12, 5], [2, 3]]) == [2, 3, 5], "list not flattening" # assert return contain correct values
    assert isinstance(mlist.flatten_list_prime.flatten_list_prime([[12, 5], [2, 3]]), list), "output not a list" # assert return is a list
    assert len(mlist.flatten_list_prime.flatten_list_prime([[12, 5], [2, 3]])) >= len([[12, 5], [2, 3]]), "length of output should not be greater than length of input"  # assert return length is less than or equal to input length
