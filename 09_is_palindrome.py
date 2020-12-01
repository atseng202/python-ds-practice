def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    lower_phrase = phrase.lower()
    remove_space = lower_phrase.split(" ")
    no_space_phrase = "".join(remove_space)

    no_space_phrase_reversed = "".join(reversed(list(no_space_phrase)))
    
    return True if no_space_phrase_reversed == no_space_phrase else False



