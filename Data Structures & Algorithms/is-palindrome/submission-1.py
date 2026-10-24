class Solution:
    def isPalindrome(self, s: str) -> bool:
        o = []
        for char in s:
            if char.isalpha() or char.isnumeric():
                o.append(char.lower())
        
        for i in range(len(o) // 2):
            if o[i] != o[len(o) -1 - i]:
                return False
        
        return True
