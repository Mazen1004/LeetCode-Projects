class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        no_duplicate = set(nums)
        
        return len(nums) != len(no_duplicate)
        