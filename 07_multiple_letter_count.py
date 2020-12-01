def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    dict_of_ltrs = {}
    for letter in phrase:
        if letter in dict_of_ltrs:
            dict_of_ltrs[letter] += 1
        else:
            dict_of_ltrs[letter] = 1

    return dict_of_ltrs