# test_binary_search.py

import pytest
import mlist

def test_format():
    with pytest.raise(TypeError):
        mlist.binary_search(4, [[1,2], [3, 5]])  # return ERROR if input is a nested list
        mlist.binary_search(4, [1,2, "hello",6,8])  # return ERROR if input contains strings
        mlist.binary_search("hello", [1,2,3,4,6,8])  # return ERROR if input contains strings

def test_values():
    with pytest.raise(TypeError):
        mlist.binary_search(3, [1,3,25,36,8, 5550])  # return ERROR if input contains values over 1000
        mlist.binary_search(3000, [1,3,25,36,8, 11])  # return ERROR if input contains values over 1000
        mlist.binary_search(3, [ 1, 3.0 , 8, 9, 15])  # return ERROR if input contains float
        mlist.binary_search(3.0, [ 1, 3 , 8, 9, 15])  # return ERROR if input contains float

def test_output():
    assert mlist.binary_search(3, [1,2 ,3, 4]) == [TRUE, 3, 4 ] # assert return contain correct values
    assert mlist.binary_search(3, [1,2, 4]) == [FALSE, 3, 0 ] # assert return contain correct values
    assert type(mlist.binary_search(3, [1,2 ,3, 4]) == "list" # assert return is a list
    assert length(mlist.binary_search([[12, 5], [2, 3]])) == 3  # assert return length is 3
