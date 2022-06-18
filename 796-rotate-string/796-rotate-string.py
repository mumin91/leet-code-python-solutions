class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        # return true if s and goal are same
        if s == goal:
            return True
        # return false if length of both strings are not same
        if len(s) != len(goal):
            return False
        
        
        for index in range(len(s)):
            
            # if any character from s is not found in goal, return False
            if s[index] not in goal:
                return False
            
            # Shift the character and check if matches
            first_char = s[0]
            sliced = s[1:]
            s = sliced + first_char
            
            if s == goal:
                return True
            
        return False
            
        
        