class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        setNums = set(nums)

        for i in range(len(nums)+1):
            if i not in setNums:
                return i     
 
        