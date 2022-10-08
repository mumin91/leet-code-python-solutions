class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        the complexity is O(n)
        """
        result = [-1, -1]
        
        try:
            result[0] = nums.index(target)
        except ValueError:
            return result
        
        for i in range(result[0], len(nums)):
            if nums[i] == target:
                result[1] = i
        
        return result
        