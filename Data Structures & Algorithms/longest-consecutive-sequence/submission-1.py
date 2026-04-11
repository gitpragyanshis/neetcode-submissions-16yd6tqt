class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0

        for i in range(len(nums)):
            curr = nums[i]
            curr_r = 0

            while curr in num_set:
                curr += 1
                curr_r += 1
            
            
            result = max(result, curr_r)
        
        return result

