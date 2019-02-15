# test_binary_search.py

import pytest
import mlist

    
def test_format():
    with pytest.raise(TypeError("Input x must be an integer.")):
        mlist.binary_search("hello", [1,2,3,4,6,8])  # return ERROR if input x is a string
        mlist.binary_search(3.0, [1,3,8,9,15])  # return ERROR if input x is a float
    with pytest.raise(TypeError("Input lst must be a list.")):
        mlist.binary_search(4, [[1,2], [3, 5]])  # return ERROR if input lst is a nested list
    with pytest.raise(TypeError("Input lst must be list of intergers.")):
        mlist.binary_search(4, [1,2, "hello",6,8])  # return ERROR if input lst contains strings
        mlist.binary_search(3, [1,3.0,8,9,15])  # return ERROR if input lst contains float
    with pytest.raise(TypeError("Input lst must be sorted.")):
        mlist.binary_search(3, [3,1,7,2,8])  # return ERROR if input lst is not sorted
    

def test_values():
    with pytest.raise(TypeError("First input contains values exceed 1000. Please limit range of input values to less than 1000.")):
        mlist.binary_search(3000, [1,3,25,36,800,900])  # return ERROR if input x is over 1000        
    with pytest.raise(TypeError("Second input contains values exceed 1000. Please limit range of input values to less than 1000.")):
        mlist.binary_search(3, [1,3,25,36,800,5550])  # return ERROR if input lst contains values over 1000

def test_output():
    assert mlist.binary_search(3, [1,2,3,4]) == [TRUE, 3, 4 ] # assert return contain correct values
    assert mlist.binary_search(3, [1,2,4]) == [FALSE, 3, 0 ] # assert return contain correct values
    assert type(mlist.binary_search(3, [1,2,3,4]) == "list" # assert return is a list
    assert length(mlist.binary_search([[12,5], [2,3]])) == 3  # assert return length is 3
