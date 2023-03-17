def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    str = ""
    
    for ltr in phrase:
        if ltr == (' '):
            return str.title()
        else:
            str += ltr
    return str.title()
    
print(f"answer should be 'Python': --> {capitalize('python')}")
print(f"answer should be 'Only first word': --> {capitalize('only first word')}")