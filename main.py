def jackie_eats(piles, hours_to_eat, avg):
    """
    checks condition if monkey can eat all bananas with eating speed of probable_speed in hours_to_eat
    :param piles: list of piles with bananas
    :param hours_to_eat: hours monkey has to eat all bananas
    :param avg: speed to check
    :return: true if pass condition else false
    >>> jackie_eats([3, 6, 7, 11], 8, 6)
    True
    >>> jackie_eats([3, 6, 7, 11], 8, 3)
    False
    """
    all_hours = 0
    for pile in piles:
        all_hours += pile // avg
        if pile % avg != 0:
            all_hours += 1
    return all_hours <= hours_to_eat


def binary_search(min_bananas, max_bananas, piles, hours):
    """
    :param min_bananas: minimal value to start search
    :param max_bananas: maximal value of bananas in piles
    :param piles: array of piles with bananas
    :param hours: hours monkey has to eat all bananas
    :return: minimal most suitable value to pass task condition
    >>> binary_search(1, 30, [30, 11, 23, 4, 20], 6)
    23
    """
    while min_bananas < max_bananas:
        avg = (min_bananas + max_bananas) // 2

        if jackie_eats(piles, hours, avg):
            max_bananas = avg
        else:
            min_bananas = avg + 1
    return min_bananas


def find_speed_to_eat_bananas(piles, hours):
    """
    :param piles: array of bananas
    :param hours: the time during which the monkey must eat all the bananas
    :return: a value that satisfies the condition
    >>> find_speed_to_eat_bananas([3, 6, 7, 11], 8)
    4
    >>> find_speed_to_eat_bananas([30, 11, 23, 4, 20], 5)
    30
    >>> find_speed_to_eat_bananas([30, 11, 23, 4, 20], 6)
    23
    >>> find_speed_to_eat_bananas([4,9,28,43],7)
    15
    """
    max_speed = 0
    for pile in piles:
        if max_speed < pile:
            max_speed = pile
    min_speed = 1

    if len(piles) == hours:
        return max_speed
    return binary_search(min_speed, max_speed, piles, hours)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
