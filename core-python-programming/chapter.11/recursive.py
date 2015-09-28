__author__ = 'weixy6'


def recursive(n):
    """
    calculate n!
    :param n:
    :return: n!
    """
    if n == 0 or n == 1:
        return 1
    else:
        return (n*recursive(n-1))


if __name__ == '__main__':
    print recursive(5)

