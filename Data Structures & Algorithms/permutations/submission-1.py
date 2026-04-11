class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, slate, result):
            if len(slate) == len(nums):
                result.append(slate.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in slate:
                    slate.append(nums[i])
                    dfs(nums, slate, result)
                    slate.pop()
        
        result, slate = [], []
        dfs(nums, slate, result)
        return result