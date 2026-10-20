class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
        """
        if len(s) != len(t):
            return False
        
        count1 = {}
        count2 = {}

        for index in range(len(s)):
            count1[s[index]] = count1.get(s[index], 0) + 1
            count2[t[index]] = count2.get(t[index], 0) + 1
        
        return count1 == count2
        """
        
        """
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
        """