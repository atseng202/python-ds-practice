def reverse_string(phrase):
    """Reverse string,

    >>> reverse_string('awesome')
    'emosewa'

    >>> reverse_string('sauce')
    'ecuas'
    """
    new_phrase = reversed(list(phrase))
    return "".join(new_phrase)
