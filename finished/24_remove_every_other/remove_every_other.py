def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    new_lst = []
    
    for x in lst:
        if x % 2 != 0:
            new_lst.append(x)
    return new_lst
    
    
    
print(f"answer should be '[1, 3, 5]': --> {remove_every_other([1, 2, 3, 4, 5])}")
