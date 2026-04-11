class TimeMap:

    def __init__(self):
        self.data_map:dict[str, List[List[int]]] = defaultdict(list) 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data_map:
            return ""
        
        start, end = 0, len(self.data_map[key])
        result = ""

        while start < end:
            mid = (start + end) // 2

            if self.data_map[key][mid][0] <= timestamp:
                start = mid + 1
                result = self.data_map[key][mid][1]
            else:
                end = mid
        
        return result
        

