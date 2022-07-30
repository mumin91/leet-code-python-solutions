class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brut force solution with N squred

        for i in range(len(nums)):
            for j in range(len(nums)):
                if j == i:
                    continue
                if (nums[j] + nums[i]) == target:
                    return [i, j]
        return []