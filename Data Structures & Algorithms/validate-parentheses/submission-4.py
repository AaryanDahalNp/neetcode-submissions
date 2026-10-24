from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        values = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        
        stack = deque()
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            
            if char in [')','}', ']']:
                if stack:
                    if values[char] != stack.pop():
                        return False
                else:
                    return False
        
        if stack:
            return False

        return True