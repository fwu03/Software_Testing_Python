# test_find_primes.py

import pytest
from mlist import find_prime

def test_no_primes():
    """
    Should return None for a list with no primes should 
    """
    assert find_prime.find_prime([0,4,6,8]) == None

def test_empty_list():
    """
    Should raise an error for an empty list
    """
    with pytest.raises(TypeError):
        find_prime.find_prime([])
        
def test_non_list():
    """
    Should raise an error for a non-list
    """
    with pytest.raises(TypeError):
        find_prime.find_prime('abcded')
        
def test_one_prime():
    """
    Should find the single prime in a list with only one prime
    """
    assert find_prime.find_prime([12,18,20.22,11]) == 11
    
def test_only_non_ints():
    """
    Should return None for a list with no integers
    """
    assert find_prime.find_prime([100.19,999.1938,-1988274783.282,37572.18]) == None
        
def test_multiple_same_primes():
    """
    Should return the single prime number in a list with the same prime number
    repeated
    """
    assert find_prime.find_prime([907,907,907,907,907,907,907]) == 907
    
def test_only_prime_big_start():
    """
    Should return the largest prime when the largest prime is at the
    start of the list
    """
    assert find_prime.find_prime([977,449,599,331,2]) == 977
    
def test_big_end():
    """
    Should return the largest prime when the largest prime is at the end
    of the list
    """
    assert find_prime.find_prime([50,449,24,727]) == 727
    
def test_only_prime_big_end():
    """
    Should return the largest prime at the start of a list when the list
    has only primes
    """
    assert find_prime.find_prime([877,449,97,599,2]) == 877
    
