import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for i in range(len(nums)):
            curr = nums[i]
            curr_length = 0
            
            if curr - 1 in s:
                continue
            
            while curr in s:
                curr = curr + 1
                curr_length += 1
                longest = max(longest, curr_length)
        
        return longest








            

