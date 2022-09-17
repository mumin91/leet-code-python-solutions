class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        zero_index_list = list()
        
        for i in range(len(arr)):
            if arr[i] == 0:
                if i in zero_index_list:
                    continue
                zero_index_list.append(i+1)
                arr.insert(i + 1, 0)
                arr.pop()