def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    # ppl_lst = []
    # for name_dict in people:
    #     ppl_lst.append(f"{name_dict['first']} {name_dict['last']}")
    # return ppl_lst

    return [f"{name_dict['first']} {name_dict['last']}" for name_dict in people]
