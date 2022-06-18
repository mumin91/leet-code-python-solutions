class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if len(part) > len(s):
            return s
        
        index = 0
        
        while index < len(s):
            if s[index:index+len(part)] == part:
                s = s.replace(part, "", 1)
                index = 0
            else:
                index += 1
        
          
            
        return s
            