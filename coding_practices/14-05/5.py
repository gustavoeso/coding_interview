# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # Só é possível criar uma árvore binária cheia com número ímpar de nós
        if n % 2 == 0:
            return []

        # Memorização para evitar recomputações
        memo = {}

        def helper(nodes):
            if nodes in memo:
                return memo[nodes]
            
            if nodes == 1:
                return [TreeNode(0)]
            
            res = []
            # Tenta todas as divisões ímpares possíveis de filhos
            for left_nodes in range(1, nodes, 2):
                right_nodes = nodes - 1 - left_nodes
                left_trees = helper(left_nodes)
                right_trees = helper(right_nodes)
                
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)

            memo[nodes] = res
            return res

        return helper(n)
