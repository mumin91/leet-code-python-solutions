class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        s = ''.join(ch.lower().replace(" ", "") for ch in s if ch.isalnum())
    
        return s == s[::-1]
            
            
        