from solution import generate_parens


def _check(n, expected):
    received = generate_parens(n)
    assert isinstance(received, list), 'generate_parens should return a list.'
    assert len(expected) == len(received), f'Number of returned solutions is different than expected for n={n}. Expected: {len(expected)}. Got: {len(received)}'
    for el in received:
        assert isinstance(el, str), 'generate_parens should return a list of strings.'
    for el in expected:
        assert el in received, f'Solution for n={n} should include string "{el}". Got: {received}.'


def test_1():
    _check(0, [''])


def test_2():
    _check(1, ['()'])


def test_3():
    _check(2, ['()()', '(())'])


def test_4():
    _check(3, ['()()()', '()(())', '(())()', '(()())', '((()))'])


def test_5():
    _check(4, ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()'])
