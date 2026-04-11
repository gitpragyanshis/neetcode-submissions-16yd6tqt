class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i in range(len(nums)):
            remaining = target - nums[i]

            if remaining in m:
                return [m[remaining], i]
            
            m[nums[i]] = i
        return None