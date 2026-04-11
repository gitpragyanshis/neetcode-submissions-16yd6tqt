class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, slate, result, index):
            result.append(slate.copy())

            for i in range(index, len(nums)):
                slate.append(nums[i])
                backtrack(nums, slate, result, i + 1)
                slate.pop()
        slate, result = [], []

        backtrack(nums, slate, result, 0)

        return result