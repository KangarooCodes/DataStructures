def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    
    for x in lst:
        if isinstance(x,list) != True:
            return False
    return True
    
    
print(f"answer should be 'True': --> {list_check([[1], [2, 3]])}")
print(f"answer should be 'False': --> {list_check([[1], 'nope'])}")