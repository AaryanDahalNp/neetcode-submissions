class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        most_frequent = []
        for times in range(k):
            highest = float('-inf')
            for key, value in counter.items():
                if value > highest:
                    highest = value
                    to_add = key

            most_frequent.append(to_add)
            del counter[to_add]
                    
        return most_frequent