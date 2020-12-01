def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

    >>> multiple_letter_count('yay')
    {'y': 2, 'a': 1}

    >>> multiple_letter_count('Yay')
    {'Y': 1, 'a': 1, 'y': 1}
    """
    ltrs_to_count = {}
    for letter in phrase:
        ltrs_to_count[letter] = ltrs_to_count.get(letter, 0) + 1
        
        # old solution
        # if letter in ltrs_to_count:
        #     ltrs_to_count[letter] += 1
        # else:
        #     ltrs_to_count[letter] = 1

    return ltrs_to_count
