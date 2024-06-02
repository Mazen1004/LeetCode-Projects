class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = {}
        for right in range(len(arr)):
            if arr[right] in counts:
                counts[arr[right]] += 1
            else:
                counts[arr[right]] = 1

        frequencies = counts.values()
        #If length of dictionary == length of set they are all unique
        if len(set(frequencies)) == len(counts):
            return True
        else:
            return False
        