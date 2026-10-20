class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        reference = {}
        for num in nums:
            if num in reference:
                return True
            reference[num] = 1
        
        return False