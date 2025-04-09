def longest_sequence(n: int) -> int:
    current = 0
    prev = 0
    max_length = 1

    while n != 0:
        if (n & 1) == 1:
            current += 1
        else:
            if(n & 2) == 2:
                prev = current
            else:
                prev = 0
            current = 0
        max_length = max(max_length, prev + current + 1)
        n >>= 1
    return max_length

print(longest_sequence(1775))
