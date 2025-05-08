from typing import List, Optional, Tuple

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class LinkedListNode:
    def __init__(self, val: int = 0, next: Optional['LinkedListNode'] = None):
        self.val = val
        self.next = next

# 1. Sum of list using pop
def list_sum(l: List[int]) -> int:
    if not l:
        return 0
    return l.pop() + list_sum(l)

# 2. Digit sum
def digit_sum(n: int) -> int:
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)

# 3. Tree sum
def tree_sum(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)

# 4. Tree max
def tree_max(root: Optional[TreeNode]) -> int:
    if not root:
        return float('-inf')
    return max(root.val, tree_max(root.left), tree_max(root.right))

# 5. K combinations
def k_combinations(l: List[int], k: int) -> List[List[int]]:
    if k == 0:
        return [[]]
    if not l:
        return []
    with_first = [[l[0]] + rest for rest in k_combinations(l[1:], k - 1)]
    without_first = k_combinations(l[1:], k)
    return with_first + without_first

# 6. All strictly increasing sequences
def all_strictly_increasing_sequences(k: int, n: int, start=1) -> List[List[int]]:
    if k == 0:
        return [[]]
    result = []
    for i in range(start, n + 1):
        for seq in all_strictly_increasing_sequences(k - 1, n, i + 1):
            result.append([i] + seq)
    return result

# 7. Create pattern
def create_pattern(n: int) -> List[int]:
    def helper(x: int) -> List[int]:
        if x <= 0:
            return [x]
        rest = helper(x - 5)
        return [x] + rest + [x]
    return helper(n)

# 8. Find middle node of linked list
def find_middle_rec(head: Optional[LinkedListNode], n: int = 0) -> Tuple[int, Optional[LinkedListNode]]:
    if not head:
        return n, None
    count, mid = find_middle_rec(head.next, n + 1)
    if n == count // 2:
        return count, head
    return count, mid
