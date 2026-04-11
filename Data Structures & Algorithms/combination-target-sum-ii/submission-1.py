class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates: List[int],slate: List[int], result: List[int], index: int, s: int, target: int):
            if s == target:
                result.append(slate.copy())
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] + s > target:
                    break
                
                slate.append(candidates[i])
                backtrack(candidates, slate, result, i + 1, s + candidates[i], target)
                slate.pop()

        result, slate = [], []
        candidates.sort()
        backtrack(candidates, slate, result, 0, 0, target)
        return result
