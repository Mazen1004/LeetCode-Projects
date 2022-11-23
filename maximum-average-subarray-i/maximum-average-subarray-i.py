class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr=avg=0
        
        
        for i in range(k): #calculates sum of first k elements
            curr += nums[i]
            i+=1
           
        ans = curr
        
        for i in range(k, len(nums)): #iterate over rest of the windows
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr) #finds max answer
    
        return ans/k #if has largest sum then it has largest avg
     
        
     
        