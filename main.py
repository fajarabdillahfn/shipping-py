import doctest


def min_cost(n, h):
    """Find min cost of delivery

    >>> min_cost(4, [1, 4, 2, 4])
    [1, 2, 2, 3]
    >>> min_cost(5, [100, 100, 100, 100, 1])
    [5, 4, 3, 2, 1]
    """

    return [min(h[j] + abs(i-j) for j in range(n)) for i in range(n)]


doctest.testmod()
