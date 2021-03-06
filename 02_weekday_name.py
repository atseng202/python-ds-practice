def weekday_name(day_of_week):
    """Return name of weekday.

        >>> weekday_name(1)
        'Sunday'

        >>> weekday_name(7)
        'Saturday'

    For days not between 1 and 7, return None

        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    # if type(day_of_week) != int or day_of_week > 7 or day_of_week < 1:
    #     return None

    # move to global constant
    days_dict = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }
    # return days_dict[day_of_week]
    return days_dict.get(day_of_week, None)
