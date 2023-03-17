def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    list = ''
    
    if phrase.count(to_swap) > 0:
        for x in phrase:
            if x.upper() == to_swap or x.lower() == to_swap:
                list += x.swapcase()
            else:
                list += x
        return list
    else:
        print("letter not in phrase, try again.")
    
print(f"answer should be  'aAAAhhh': --> {flip_case('Aaaahhh', 'a')}")
print(f"answer should be  'aAAAhhh': --> {flip_case('Aaaahhh', 'A')}")
print(f"answer should be  'AaaaHHH': --> {flip_case('Aaaahhh', 'h')}")
{flip_case('Aaaahhh', 'r')}