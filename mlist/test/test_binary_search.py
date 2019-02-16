# test_binary_search.py

import pytest
from mlist import binary_search

    
def test_format():
    with pytest.raises(TypeError):
        binary_search.binary_search("hello", [1,2,3,4,6,8])  # return ERROR if input x is a string
        binary_search.binary_search(3.0, [1,3,8,9,15])  # return ERROR if input x is a float
    with pytest.raises(TypeError):
        binary_search.binary_search(4, [[1,2], [3, 5]])  # return ERROR if input lst is a nested list
    with pytest.raises(TypeError):
        binary_search.binary_search(4, [1,2, "hello",6,8])  # return ERROR if input lst contains strings
        binary_search.binary_search(3, [1,3.0,8,9,15])  # return ERROR if input lst contains float
    with pytest.raises(ValueError):
        binary_search.binary_search(3, [3,1,7,2,8])  # return ERROR if input lst is not sorted
    

def test_values():
    with pytest.raises(ValueError):
        binary_search.binary_search(3000, [1,3,25,36,800,900])  # return ERROR if input x is over 1000        
    with pytest.raises(ValueError):
        binary_search.binary_search(3, [1,3,25,36,800,5550])  # return ERROR if input lst contains values over 1000

def test_output():
    # assert return contain correct values
    assert binary_search.binary_search(3, [1,2,3,4]) == [True,3,2], "Assertion Failed, the output is wrong"
    # assert return contain correct values
    assert binary_search.binary_search(3, [1,2,4]) == [False,3,0], "Assertion Failed, the output is wrong"
    # assert return is a list
    assert isinstance(binary_search.binary_search(3, [1,2,3,4]), list), "Assertion Failed, the output should be a list"
    # assert return length is 3
    assert len(binary_search.binary_search(2, [2,3])) == 3, "Assertion Failed, the output has incorrect length"
