class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        # Lista de tuplas: (bitmask, comprimento da palavra)
        masks = [0] * n
        lengths = [len(word) for word in words]

        for i, word in enumerate(words):
            for c in word:
                # Marca o bit da letra c
                masks[i] |= 1 << (ord(c) - ord('a'))

        max_prod = 0
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    max_prod = max(max_prod, lengths[i] * lengths[j])

        return max_prod
