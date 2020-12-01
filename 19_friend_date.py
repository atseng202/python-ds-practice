def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    friend_1_hobbies = set(a[2])
    friend_2_hobbies = set(b[2])
    # one liner solution
    return bool(friend_1_hobbies & friend_2_hobbies)

    # Old solution
    # if friend_1_hobbies & friend_2_hobbies:
    #     return True
    
    # return False
