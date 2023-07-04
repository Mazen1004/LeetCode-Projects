class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
       
        ans=10000
        
        for letter in text:
            if letter in counts:
                counts[letter] +=1
        print(counts)
        
        ans=min(counts['b'], counts['a'], counts['l'] // 2, counts['o'] // 2, counts['n'])
    
        return ans