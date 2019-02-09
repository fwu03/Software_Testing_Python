# test_find_primes.py

import pytest

def test_no_primes():
    assert find_primes([0, 4, 6, 8]) == None

def test_empty_list():
    with pytest.raises(TypeError):
        find_primes([])
        
def test_non_list():
    pass
    