from pgen import gen_pass


def test_gen_pass():
    """
    >>> gen_pass('k', 'n')
    '6b0a2256a0'
    >>> gen_pass('k', 'n') == gen_pass('k', 'n')
    True
    >>> gen_pass('k', 'n', 's') != gen_pass('k', 'm', 's')
    True
    >>> len(gen_pass('k', 'n'))
    10
    >>> len(gen_pass('k', 'n', length=15))
    15
    >>> gen_pass('k', 'n', length=666)
    Traceback (most recent call last):
        ...
    ValueError: length (666) > MAX_LENGTH (56)
    """
    pass