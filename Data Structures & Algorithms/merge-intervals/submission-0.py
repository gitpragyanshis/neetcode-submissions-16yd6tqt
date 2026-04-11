class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        result.append(intervals[0])

        for i in range(1, len(intervals)):
            c_s, c_e = intervals[i]

            if c_s <= result[-1][1]:
                n_s =  min(result[-1][0], c_s)
                n_e = max(result[-1][1], c_e)

                result.pop()
                result.append([n_s, n_e])
            else:
                result.append([c_s, c_e])
        

        return result

