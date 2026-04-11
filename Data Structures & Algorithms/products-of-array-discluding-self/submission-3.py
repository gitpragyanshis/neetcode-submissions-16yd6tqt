class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        prev = 1

        for i in range(0, len(result)):
            result[i] = prev
            prev = result[i] * nums[i]

        prev = 1
        for j in range(len(result) - 1, -1, -1):
            result[j] *= prev
            prev = nums[j] * prev
         
        return result

