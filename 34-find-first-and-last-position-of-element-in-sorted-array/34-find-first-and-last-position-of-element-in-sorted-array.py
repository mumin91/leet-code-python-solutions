class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        the complexity is O(log n) with binary 
        """
        first_occurence = self.findBound(nums, target, True)
        if (first_occurence == -1):
            return [-1, -1]
        
        last_occurence = self.findBound(nums, target, False)
        
        return [first_occurence, last_occurence]
    
    
    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        
        length_of_nums = len(nums)
        index_start = 0
        index_end = length_of_nums - 1
        
        while index_start <= index_end:
            index_mid = (index_start + index_end) // 2   
            
            if nums[index_mid] == target:
                
                if isFirst:
                    # This means we found our lower bound.
                    if index_mid == index_start or nums[index_mid - 1] < target:
                        return index_mid

                    # Search on the left side for the bound.
                    index_end = index_mid - 1
                else:
                    
                    # This means we found our upper bound.
                    if index_mid == index_end or nums[index_mid + 1] > target:
                        return index_mid
                    
                    # Search on the right side for the bound.
                    index_start = index_mid + 1
            
            elif nums[index_mid] > target:
                index_end = index_mid - 1
            else:
                index_start = index_mid + 1
        
        return -1 
        