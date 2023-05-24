class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_ = {}

        for key, num in enumerate(nums):
            temp = target - num
            if temp in  dict_:
                return [dict_[temp], key]
            
            dict_[num] = key
        return None