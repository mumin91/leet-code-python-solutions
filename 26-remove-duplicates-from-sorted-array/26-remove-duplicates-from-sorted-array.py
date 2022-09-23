class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        length_of_nums_list = len(nums)
        
        while index < length_of_nums_list:
            if nums[index] in nums[:index]:
                nums.pop(index)
                length_of_nums_list = len(nums)
            else:
                index += 1
                
        return length_of_nums_list
            
        