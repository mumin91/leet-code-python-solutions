class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        s = s.lower()
        s = ''.join(ch for ch in s if ch.isalnum())
        s = s.replace(" ", "")
    
        return s == s[::-1]
            
            
        