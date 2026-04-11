class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(nums, slate, result, total, target, index):
            if total == target:
                result.append(slate.copy())
                return 
            
            for i in range(index, len(nums)):
                if total + nums[i] > target:
                    return
                slate.append(nums[i])
                backtrack(nums, slate, result, total + nums[i],target,  i)
                slate.pop()
        
        slate, result = [], []
        nums.sort()
        backtrack(nums, slate, result, 0, target, 0)
        return result