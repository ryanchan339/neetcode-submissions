class TimeMap:

    def __init__(self):
        self.vals = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.vals:
            self.vals[key] = []
        self.vals[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.vals:
            return ""
        arr = self.vals[key]
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            if arr[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        if l == 0:
            return ""
        return arr[l - 1][1]

        #1 2 4 5 6


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)