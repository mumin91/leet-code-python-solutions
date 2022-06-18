# Solved with sliding window 
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        
        if not word:
            return 0
        
        vowel_count_set = set()
        length_of_the_longest_beautiful_substring = 0
        lower_index = -1
            
        for index in range(len(word)):
            current_vowel_character = word[index]
            previous_vowel_character = word[index-1]
            
            if index > 0 and current_vowel_character < previous_vowel_character:
                # empty the set
                vowel_count_set = set()
                lower_index = index - 1
                
            vowel_count_set.add(current_vowel_character)    
            if len(vowel_count_set) == 5:
                length_of_the_longest_beautiful_substring = max(length_of_the_longest_beautiful_substring, index - lower_index)
                
        return length_of_the_longest_beautiful_substring
                
                
        