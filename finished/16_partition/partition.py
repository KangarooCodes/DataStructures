def is_even(num):
        return num % 2 == 0     
      
def is_string(el):
        return isinstance(el, str)
    
def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    
    if fn == is_even:
        evens = []
        odds = []
        answer = [evens,odds]
        for x in lst:
            if is_even(x) == True:
                evens.append(x)
            else:
                odds.append(x)
        return answer
                        
    if fn == is_string:
       yes_string = []
       not_string = []
       answer = [yes_string,not_string]
       for x in lst:
           if is_string(x) == True:
               yes_string.append(x)
           else:
               not_string.append(x)
    return answer
    
    
print(f"answer should be '[[2, 4], [1, 3]]': --> {partition([1, 2, 3, 4], is_even)}")
print(f"answer should be '[['hi', 'bye'], [None, 6]]': --> {partition(['hi', None, 6, 'bye'], is_string)}")