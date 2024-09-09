class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        apples = 0 
        currentWeight = 0
        weight.sort()
        
        for apple in weight:
            if apple + currentWeight <= 5000:
                currentWeight = currentWeight + apple
                apples += 1
            else:
                break

        return apples
            