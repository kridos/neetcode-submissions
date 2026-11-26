from collections import Counter
class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        counts = Counter(nums)
        
        for num, count in counts.items():
            buckets[count].append(num)

        res = []

        for i in range(len(nums), -1, -1):
            for num in buckets[i]:
                if len(res) == k:
                    return res
                
                res.append(num)

        return res

