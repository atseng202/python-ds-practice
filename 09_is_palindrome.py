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
    # lowercase, then replace all spaces in string, and use slicing to reverse
    lower_phrase = phrase.lower()
    no_space_phrase =lower_phrase.replace(" ", "")
    no_space_phrase_reversed = no_space_phrase[::-1]
    return no_space_phrase_reversed == no_space_phrase
    
    # remove_space = lower_phrase.split(" ")
    # no_space_phrase = "".join(remove_space)
    # no_space_phrase_reversed = "".join(reversed(list(no_space_phrase)))
    



