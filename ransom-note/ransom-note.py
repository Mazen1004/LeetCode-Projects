class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ans = True
        magazine_count ={}
        ransom_count={}
        
        for i in magazine:
            magazine_count[i] = magazine_count.get(i,0)+1
        
        for i in ransomNote:
            ransom_count[i] = ransom_count.get(i,0)+1
            
        print(magazine_count)
        print(ransom_count)
        
        for key in ransom_count:
            if key not in magazine_count or ransom_count[key] > magazine_count[key]:
                ans = False
        
        return ans