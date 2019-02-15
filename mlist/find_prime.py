# find_prime.py

import mlist.__init__ as __init__

def find_prime(x):
    """
      Usage: Find largest prime numbers within a list of integer.

       Argument:

            x : a list of integer.

       Return:
      
            an integer

       Examples:

       find_prime([0,1,2,3,4,5])
       >>>5

       find_prime([0,1])
       >>> "No prime number in list"

       find_prime(["hello", 1, 5])
       >>> "Exception error: input list must contains only integers"
    """
    
    prime = __init__.get_prime()
    
    # Raise error if input not a list
    if type(x) != list:
        raise TypeError("Input must be a list")

    # Raise error if input is not integer (eg. float, string...)
    for i in x:
        if type(i) != int:
            raise TypeError("Input must be list of intergers")
            
    # Raise error if input values less than 1000
    if max(x) >= 1000:
        raise ValueError("Input values exceed 1000. Please limit range of input values to less than 1000.")
    
    #return list of prime numbers
    max_prime = list(set(x).intersection(prime))
    
    #return the largest prime numbers
    if len(max_prime) >=1:
        return max(max_prime)
    else:
        return "No prime number in list"
    
    