def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    
    phrase = phrase.lower()
    vowels = 'aeiou'
    ltr_count = {vowel: 0 for vowel in vowels}
    
    for ltr in phrase:
        if ltr in vowels != False:            
            ltr_count[f"{ltr.lower()}"] += 1
    return (ltr_count)

            
    
    
    
print(f"answer should be '('i': 1, 'o': 2)': --> {vowel_count('rithm school')}")
print(f"answer should be '('o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1)': --> {vowel_count('HOW ARE YOU? i am great!')}")