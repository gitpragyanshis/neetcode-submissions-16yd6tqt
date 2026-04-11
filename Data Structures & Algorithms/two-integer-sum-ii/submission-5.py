class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1

        while start < end:
            current = numbers[start] + numbers[end]
            if current == target:
                return [start+1, end+1]
            elif current > target:
                end -= 1
            else:
                start += 1
        
        return None


