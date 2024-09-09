from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arrSizeGoal = round(len(arr) / 2)
        count = 0

        counts = Counter(arr)
        ordered = sorted(counts.values(), reverse=True)

        currArrSize= len(arr)
        for frequency in ordered:
            count += 1
            if currArrSize - frequency <= arrSizeGoal: #condition has been met so couunt can be returned
                return count
            else:
                currArrSize = currArrSize - frequency

        