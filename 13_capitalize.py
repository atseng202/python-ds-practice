def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

    >>> capitalize('python')
    'Python'

    >>> capitalize('only first word')
    'Only first word'
    """
    # Slice string is probably better, capitalize first letter + rest of string
    # return phrase[0].capitalize() + phrase[1:]
    # or maybe just do phrase.capitalize()
    return phrase.capitalize()