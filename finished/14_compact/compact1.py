def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    return [val for val in lst if val]

print(f"answer should be '[1, 2, 'All done']': --> {compact([0, 1, 2, '', [], False, (), None, 'All done'])}")