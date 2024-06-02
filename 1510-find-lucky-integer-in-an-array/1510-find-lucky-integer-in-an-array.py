class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = {}
        for right in range(len(arr)):
            if arr[right] in counts:
                counts[arr[right]] += 1
            else:
                counts[arr[right]] = 1

        luckynum = -1
        for key, value in counts.items():
            if key == value:
                luckynum = max(luckynum, value)
        
        return luckynum