class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        reference = set()
        for num in nums:
            if num in reference:
                return True
            reference.add(num)
        return False