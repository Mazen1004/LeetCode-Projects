class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = {}
        for right in range(len(nums)):
            if nums[right] in counts:
                counts[nums[right]] += 1
            else:
                counts[nums[right]] = 1

        uniqueSum = 0
        print(counts)
        for key, value in counts.items():
            if value == 1:
                uniqueSum += key

        return uniqueSum