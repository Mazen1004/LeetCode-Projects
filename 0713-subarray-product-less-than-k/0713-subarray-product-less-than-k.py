class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = left = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while left <= right and curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1

        return ans