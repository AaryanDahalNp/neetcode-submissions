class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = set(nums)
        for i in range(len(nums)):
            if (target - nums[i]) in hashset:
                for j in range(len(nums)):
                    if i == j:
                        continue
                    if nums[i] + nums[j] == target:
                        return [i, j]