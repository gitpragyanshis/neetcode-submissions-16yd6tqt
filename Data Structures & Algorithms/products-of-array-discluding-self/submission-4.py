class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        prev = 1

        for i in range(len(nums)):
            result[i] = prev
            prev = prev * nums[i]

        prev = 1

        for j in range(len(nums) - 1, -1, -1):
             result[j] *= prev
             prev *= nums[j]
        

        return result