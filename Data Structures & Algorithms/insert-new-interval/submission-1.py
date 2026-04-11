class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        n_s, n_e = newInterval

        for i in range(len(intervals)):
            c_s, c_e = intervals[i]
            if n_e < c_s:
                result.append([n_s, n_e])
                return result + intervals[i:]
            elif n_s > c_e:
                result.append(intervals[i])
            else:
                n_s, n_e = min(n_s, c_s), max(n_e, c_e)
        
        result.append([n_s, n_e])
        return result
