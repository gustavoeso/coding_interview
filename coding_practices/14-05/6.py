class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = set()
        prev = set()

        for num in arr:
            curr = set()
            for val in prev:
                curr.add(val | num)
            curr.add(num)
            res.update(curr)
            prev = curr

        return len(res)
