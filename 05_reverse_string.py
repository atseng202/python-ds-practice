def reverse_string(phrase):
    """Reverse string,

    >>> reverse_string('awesome')
    'emosewa'

    >>> reverse_string('sauce')
    'ecuas'
    """
    # slice with strings
    return phrase[::-1]

    # old solution
    # new_phrase = reversed(list(phrase))
    # return "".join(new_phrase)
