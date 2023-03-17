def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    
    dict = {}
    for ltr in phrase:
        dict[ltr] = dict.get(ltr, 0) + 1
    return dict
        
    
print(f"answer should be '['y': 2, 'a': 1]': --> {multiple_letter_count('yay')}")
print(f"answer should be '['Y': 1, 'a': 1, 'y': 1]': --> {multiple_letter_count('Yay')}")