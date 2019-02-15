# binary_search.py

def binary_search(x, lst):
    '''
      Usage: The function applies the generic binary search algorithm to search if the value
      x exists in the lst, and returns a list contains: TRUE/FAlSE depends on whether the x value has been found,
      x value, and x position indice in list

      Argument:

           x: numeric
           lst: sorted list of numerics

      Return:

           a list contains:
            - first element is a logical value (TRUE/FALSE)
            - second element is a numeric value of x
            - third element is a numeric in range of 0 to length(list) where 0 indicates the element is not in the list

      Examples:

      binary_search(4, [1,2,3,4,5,6])
      >>> [TRUE,4,3]

      binary_search(5, [10,100,200,300])
      >>> [FALSE,5,0]

    '''
    # Raise error if input x is not integer
    if type(x) != int:
        raise TypeError("Input x must be an integer.")
    
    # Raise error if input lst not a list
    if type(lst) != list:
        raise TypeError("Input lst must be a list.")

    # Raise error if input lst contains non-integer (eg. float, string...)
    for i in lst:
        if type(i) != int:
            raise TypeError("Input lst must be list of intergers.")
            
    # Raise error if input lst contains values greater or equal to 1000
    if max(lst) >= 1000:
        raise ValueError("Input lst contains values exceed 1000. Please limit range of input values to less than 1000.")

    # Raise error if input lst is not sorted
    if lst != sorted(list):
        raise ValueError("Input lst must be sorted.")
    
    # ---------------------------
    # Binary Search Algorithm
    # ---------------------------
    
    # Empty list
    if len(lst) == 0:
        return [False, x, 0]
    
    low = 0
    high = len(lst)-1
    
    while low <= high:
        mid = (low + high) //2
        if lst[mid] < x:
            low = mid + 1
        elif x < lst[mid]:
            high = mid - 1
        else:
            return [True, x, mid]
    return [False, x, 0]
