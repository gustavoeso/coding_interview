# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        from collections import defaultdict

        self.count = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # soma 0 já existe no começo

        def dfs(node, curr_sum):
            if not node:
                return

            curr_sum += node.val
            self.count += prefix_sums[curr_sum - targetSum]

            prefix_sums[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            prefix_sums[curr_sum] -= 1  # backtrack

        dfs(root, 0)
        return self.count
