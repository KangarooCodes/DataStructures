def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    
    factor = []
    start = 1
    
    while start <= num:
        if (((num/start) * 10) == (int((num/start)) * 10)) is True:
            factor.append(start)
        start += 1
    return factor
    
    
    
print(f"answer should be '[1, 2, 5, 10]': --> {find_factors(10)}")
print(f"answer should be '[1, 11]': --> {find_factors(11)}")
print(f"answer should be '[1, 3, 37, 111]': --> {find_factors(111)}")
print(f"answer should be '[1, 293, 1097, 321421]': --> {find_factors(321421)}")