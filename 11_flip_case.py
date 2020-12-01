def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

    >>> flip_case('Aaaahhh', 'a')
    'aAAAhhh'

    >>> flip_case('Aaaahhh', 'A')
    'aAAAhhh'

    >>> flip_case('Aaaahhh', 'h')
    'AaaaHHH'

    """
    letters = list(phrase)
    for idx in range(0, len(letters)):
        letter = letters[idx]
        # check if letter needs to be swapped
        if letter.lower() == to_swap.lower():
            letters[idx] = letters[idx].swapcase()

    return "".join(letters)
