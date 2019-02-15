# flatten_list_prime.py

import mlist.__init__ as __init__

def flatten_list_prime(l):
    """
    Flattens a list so that all prime numbers in embedded lists are 
        returned in a flat list
    
    Parameters:
        - l: a list of numbers; largest prime cannot be greater than 1000
    
    Returns:
        - flat_l: a flat list that has all the prime numbers in l
        
    Examples:
        a = [[2, 3, 4, 5], 19, [131, 127]]
        flatten_list_prime(a) # returns [2, 3, 5, 19, 131, 127]
    """
    
    # Raise error if input not a list
    if type(l) != list:
        raise TypeError("Input must be a list")                 
    l_copy = l[:]
    
    # flatten list in the loop
    flat_l = []
    prime = __init__.get_prime()
    while len(l_copy) >= 1:
        elem = l_copy.pop()
        if not isinstance(elem, int) and not isinstance(elem, list):
            raise TypeError("Input must be list of intergers")
        if isinstance(elem, list):
            l_copy.extend(elem)
        else:
            if elem >= 1000:
                raise ValueError("Input values exceed 1000. Please limit range of input values to less than 1000.")                
            if elem in prime:
                flat_l.append(elem)
    flat_l.sort()
    return flat_l