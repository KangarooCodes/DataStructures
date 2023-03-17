def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    up = word.upper()
    return up.count(letter.upper())    
    
print(f"answer should be 1: --> {single_letter_count('Hello World', 'h')}")
print(f"answer should be 0: --> {single_letter_count('Hello World', 'z')}")
print(f"answer should be 3: --> {single_letter_count('Hello World', 'l')}")