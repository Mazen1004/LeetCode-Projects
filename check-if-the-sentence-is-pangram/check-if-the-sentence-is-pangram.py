class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dic ={}
        
        for i in range(len(sentence)):
            c=sentence[i]
            print(c)
            if c not in dic.values():
                dic[i]=c
        print(dic)
        print(len(dic))
            
        if len(dic) == 26:
            return True 
        else:
            return False