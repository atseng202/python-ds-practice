def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    numbers_count = {}
    val = 0
    key = None
    for number in nums:
        numbers_count[number] = numbers_count.get(number, 0) + 1

    for k, v in numbers_count.items():
        if v > val:
            val = v
            key = k

    return key
