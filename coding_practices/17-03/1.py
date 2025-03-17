class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = -1

        if len(nums) <= 1:
            return None
        
        for num1 in nums:
            index1 += 1
            index2 = 0
            for num2 in nums:
                if (num2 + num1) == target and index1 != index2:
                    return(index1, index2)
                index2 += 1