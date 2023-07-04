class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        unique_count = {}
        #If no unique returns -1
        ans=-1
        
        for num in nums:
            unique_count[num] = unique_count.get(num,0)+1
            
            #print(unique_count)
            
        for i in unique_count:
            if unique_count[i] == 1:
                ans = max(ans,i)
            
        return ans
                
            
                