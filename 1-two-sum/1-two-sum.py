class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, item in enumerate(nums):
            if (target - item) == item:
                if len(nums) == 2:
                    return [0, 1]
                elif nums.count(item) > 1:
                    indices = [i for i, x in enumerate(nums) if x == item]
                    return indices
                else:
                    continue
            if (target - item) in nums:
                b = target - item
                k =  nums.index(b)
                return [i,k]