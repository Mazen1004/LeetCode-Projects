class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = {}
        for arr in nums:
            for num in arr:
                if num in counts:
                    counts[num] += 1
                else:
                    counts[num] = 1
        
        n = len(nums)
        ans = []
        for key in counts:
            if counts[key] == n:
                ans.append(key)
        
        return sorted(ans)