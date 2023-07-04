from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        counts = defaultdict(int)
        #counts = {int}
        
        for player in matches:
            winner=player[0]
            loser=player[1]
            counts[winner] +=0
            counts[loser] +=1
            #print(counts)
            #print(loser)
        
        ans =[]
        lose_0=[]
        lose_1=[]
        for loses in counts:
            if counts[loses] == 0:
                lose_0.append(loses)
            if counts[loses] == 1:
                lose_1.append(loses)
        
        lose_0.sort()
        lose_1.sort()
        ans.append(lose_0)
        ans.append(lose_1)
        return ans