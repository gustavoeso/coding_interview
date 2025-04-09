from solution import swap_odd_even_bits


def _check(n_bin, expected_bin):
    n = int(n_bin, base=2)
    expected = int(expected_bin, base=2)
    received = swap_odd_even_bits(n)

    msg = f'Wrong answer for {n:b}. Expected: {expected:b}. Got: {received:b}.'
    assert expected == received, msg


def test_1():
    a = '00000000000000000000000000000000'
    b = '00000000000000000000000000000000'
    _check(a, b)
    _check(b, a)


def test_2():
    a = '10101010101010101010101010101010'
    b = '01010101010101010101010101010101'
    _check(a, b)
    _check(b, a)


def test_3():
    a = '11100011100011100011100011100011'
    b = '11010011010011010011010011010011'
    _check(a, b)
    _check(b, a)


def test_4():
    a = '10011001100110011001100110011001'
    b = '01100110011001100110011001100110'
    _check(a, b)
    _check(b, a)


def test_5():
    a = '11111111111111111111111111111111'
    b = '11111111111111111111111111111111'
    _check(a, b)
    _check(b, a)
