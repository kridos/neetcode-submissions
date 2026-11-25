class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}

        for i, num in enumerate(nums):
            remainder = target - num

            if remainder in sumMap:
                return [sumMap[remainder], i]

            sumMap[num] = i

        return [0,0]

        