def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.
    """

    if n % 50 == 0:
        return n // 50
    elif n > 0:
        return n // 50 + 1
    elif n == 0 or n < 0:
        return 0


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.
    """

    gains = 0
    losses = 0
    for op in price_changes:
        if op > 0:
            gains += op
        else:
            losses += op
    
    return (gains, losses)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.
    """

    for index in range(k):
        s = L[index]
        e = L[-1 - index]
        L[index] = e
        L[-1 - index] = s


if __name__ == '__main__':
    import doctest
    doctest.testmod()
