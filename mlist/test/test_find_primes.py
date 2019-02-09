# test_find_primes.py

import pytest
from mlist import find_prime

def test_no_primes():
    assert find_prime.find_prime([0, 4, 6, 8]) == None

def test_empty_list():
    with pytest.raises(TypeError):
        find_prime.find_prime([])
        
def test_non_list():
    with pytest.raises(TypeError):
        find_prime.find_prime('abcded')
        
def test_one_prime():
    assert find_prime.find_prime([12, 18, 20.22, 11]) == 11
    
def test_only_non_ints():
    with pytest.raises(TypeError):
        find_prime.find_prime([100.19, 999.1938, -1988274783.282, 37572.18])
        
def test_multiple_same_primes():
    assert find_prime.find_prime([907, 907, 907, 907, 907, 907, 907]) == 907
    
def test_only_prime_big_start():
    assert find_prime.find_prime([977, 449, 599, 331, 2]) == 977
    
def test_big_end():
    assert find_prime.find_prime([50, 449, 24, 727]) == 727
    
def test_only_prime_big_end():
    assert find_prime.find_prime([877, 449, 97, 599, 2]) == 877
    