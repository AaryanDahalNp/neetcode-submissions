class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset = {}
        for char in s:
            if char not in hashset:
                hashset[char] = 1
            else:
                hashset[char] += 1
        
        for char in t:
            if char not in hashset:
                return False
            if hashset[char] == 1:
                hashset.pop(char)
            else:
                hashset[char] -= 1
        
        if len(hashset) == 0:
            return True
        
        return False