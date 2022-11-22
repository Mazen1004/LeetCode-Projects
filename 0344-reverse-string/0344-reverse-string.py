class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        left=0
        right=len(s)-1
        temp=""
        
        while left < right:
            #if s[left] != s[right]: unneccessary as it causes problems with incrementing/decrementing
            temp = s[right] #stores right in temp var
            s[right] = s[left] #copies left in right
            s[left] = temp #copies temp right in left
            right-=1
            left+=1
        return s
        