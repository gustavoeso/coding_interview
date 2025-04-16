from solution import StackWithMin


def peek_min(stack, expected):
    if not expected:
        assert stack.empty(), "Stack should be empty, but isn't"
        return

    assert not stack.empty(), "Stack shouldn't be empty, but empty() returned True."
    expected_peek = expected[-1]
    user_peek = stack.peek()
    assert expected_peek == user_peek, f"Error on peek. Expected: {expected_peek}. Returned: {user_peek}."

    expected_min = min(expected)
    user_min = stack.minimum()
    assert expected_min == user_min, f"Error on minimum. Expected: {expected_min}. Returned: {user_min}. Stack: {expected}"


def check(*ops):
    stack = StackWithMin()
    expected = []
    for op, *args in ops:
        peek_min(stack, expected)
        if op == 'push':
            val = args[0]
            stack.push(val)
            expected.append(val)
        elif op == 'pop':
            p1 = stack.pop()
            p2 = expected.pop()
            assert p1 == p2, f"Error on pop. Expected: {p1}. Returned: {p2}."
        peek_min(stack, expected)


def test_1():
    check(
        ('push', 1),
        ('pop',)
    )


def test_2():
    check(
        ('push', 5),
        ('push', 4),
        ('push', 3),
        ('push', 2),
        ('push', 1),
        ('pop',),
        ('pop',),
        ('pop',),
        ('pop',),
        ('pop',),
    )


def test_3():
    check(
        ('push', 5),
        ('push', 6),
        ('push', 3),
        ('push', 7),
        ('pop',),
        ('pop',),
        ('pop',),
        ('pop',),
    )


def test_4():
    check(
        ('push', 1),
        ('push', 1),
        ('push', 1),
        ('push', 1),
        ('pop',),
        ('pop',),
        ('pop',),
        ('pop',),
    )


def test_5():
    push = []
    for i in range(1, 11):
        push.append(('push', i))
        push.append(('push', 10-i+1))
    check(*(tuple(push) + ('pop',)*len(push)))


def test_6():
    push = []
    for i in range(1, 11):
        for _ in range(5):
            push.append(('push', i))
        for _ in range(5):
            push.append(('push', 10-i+1))
    check(*(tuple(push) + ('pop',)*len(push)))


def test_7():
    peek_min(StackWithMin(), [])


def test_8():
    check(
        ('push', -1),
        ('push', -1),
        ('push', -1),
        ('push', -1),
        ('pop',),
        ('pop',),
        ('pop',),
        ('pop',),
    )


def test_9():
    push = []
    for i in range(1, 11):
        push.append(('push', -(10-i+1)))
        push.append(('push', -i))
    check(*(tuple(push) + ('pop',)*len(push)))


def test_10():
    push = []
    for i in range(1, 11):
        for _ in range(5):
            push.append(('push', -(10-i+1)))
        for _ in range(5):
            push.append(('push', -i))
    check(*(tuple(push) + ('pop',)*len(push)))
