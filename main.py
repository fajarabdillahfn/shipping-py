import doctest


def min_cost(n, h):
    """Find min cost of delivery

    >>> min_cost(4, [1, 4, 2, 4])
    [1, 2, 2, 3]
    >>> min_cost(5, [100, 100, 100, 100, 1])
    [5, 4, 3, 2, 1]
    """

    res = []
    for i in range(n):
        minimal_cost = h[i]
        for j in range(n):
            if i == j:
                continue
            else:
                city_range = abs(i-j)
                cost = h[j] + city_range

                if cost < minimal_cost:
                    minimal_cost = cost
        res.append(minimal_cost)

    return res


doctest.testmod()
