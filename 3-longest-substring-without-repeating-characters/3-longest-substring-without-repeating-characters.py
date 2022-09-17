class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length_of_s = len(s)
        result = 0
        
        count_of_chars = dict()
        
        i = 0
        
        for j in range(length_of_s):
            current_char = s[j]
            
            if current_char in count_of_chars:
                i = max(count_of_chars[current_char], i)
                
            result = max(result, j - i + 1)
            count_of_chars[current_char] = j + 1
            
        return result
            
            
        