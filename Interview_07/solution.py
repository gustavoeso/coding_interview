def generate_parens(n: int) -> list[str]:
    def add_parens(left, right, result):
        if left == n and right == n:
            result.append(''.join(current))
            return
        if left < n:
            current.append('(')
            add_parens(left + 1, right, result)
            current.pop()
        if right < left:
            current.append(')')
            add_parens(left, right + 1, result)
            current.pop()

    result = []
    current = []
    add_parens(0, 0, result)
    return result
