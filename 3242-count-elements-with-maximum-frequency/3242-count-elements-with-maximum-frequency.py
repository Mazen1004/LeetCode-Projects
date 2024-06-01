class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = {}
        maxfrequency = 0
        for right in range(len(nums)):
            if nums[right] in counts:
                counts[nums[right]] += 1
            else:
                counts[nums[right]] = 1
            #max count
            maxfrequency = max(maxfrequency, counts[nums[right]])

        frequencyCount = 0
        for key, value in counts.items():
            if value == maxfrequency:
                frequencyCount += value

        return frequencyCount