import heapq
import math

class Solution:
    def minStoneSum(self, stones: List[int], k: int) -> int:
        stones = [-stone for stone in stones] #negative to simulate maxheap
        heapq.heapify(stones)

        count = 0

        while count < k:
            x = heapq.heappop(stones)
            heapq.heappush(stones, math.floor(-abs(x/2)))
            count += 1

        return -sum(stones) #negative to convert values back from maxheap