def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    
    lst = []
    
    for num in l1:
        if l2.count(num) > 0:
            lst.append(num)
    return lst
        
    
print(f"answer should be '[2, 3]': --> {intersection([1, 2, 3], [2, 3, 4])}")
print(f"answer should be '[1, 2, 3]': --> {intersection([1, 2, 3], [1, 2, 3, 4])}")
print(f"answer should be '[3]': --> {intersection([1, 2, 3], [3, 4])}")
print(f"answer should be '[]': --> {intersection([1, 2, 3], [4, 5, 6])}")