class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = list()
        self.backtrack(nums, list(), result, 0)
        return result

    def backtrack(self, nums: List[int], slate: List[int], result: List[List[int]], index) -> None:
        result.append(slate.copy())
        
        for i in range(index, len(nums)):            
            slate.append(nums[i])
            self.backtrack(nums, slate, result, i + 1)
            slate.pop()
        


        