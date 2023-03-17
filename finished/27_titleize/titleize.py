def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    
    return phrase.title()
    
    
    
print(f"answer should be 'This Is Awesome': --> {titleize('this is awesome')}")
print(f"answer should be 'Only Capitalize First': --> {titleize('oNLy cAPITALIZe fIRSt')}")