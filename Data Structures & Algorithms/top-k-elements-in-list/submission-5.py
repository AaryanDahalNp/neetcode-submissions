class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        frequency = [[] for _ in range(len(nums) + 1)]

        for key, value in counter.items():
            frequency[value].append(key)
        
        most_frequent = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                most_frequent.append(num)
                if len(most_frequent) == k:
                    return most_frequent
                    