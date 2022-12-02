class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        startValue = 0
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1]) #finding prefix sum
            
        #min value of prefix array is -4
        minvalue = min(prefix) #returns min value of array
            
        if (minvalue > 0):
            StartValue=1
        else:
            StartValue = abs(minvalue)+1
            
        return StartValue