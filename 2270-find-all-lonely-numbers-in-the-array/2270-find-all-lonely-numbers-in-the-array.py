class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        ans = []
        numset = set(nums)
        num_count = {}

        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        for num in nums:
            if (num + 1 not in numset) and (num - 1 not in numset) and num_count[num] == 1:
                ans.append(num)
            
        return ans


