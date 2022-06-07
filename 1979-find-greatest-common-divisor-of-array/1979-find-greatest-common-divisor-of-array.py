class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums = sorted(nums)
        import math
        return math.gcd(nums[0],  nums[-1])

        