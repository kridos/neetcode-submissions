class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numLen = len(nums)
        prefixProduct = [1] * numLen
        suffixProduct = [1] * numLen

        for i in range(1, numLen):
            prefixProduct[i] = prefixProduct[i - 1] * nums[i - 1]

        for i in range(1, numLen):
            suffixProduct[i] = suffixProduct[i - 1] * nums[numLen - i]

        res = []

        for i in range(numLen):
            res.append(prefixProduct[i] * suffixProduct[numLen - 1 - i])

        return res
        