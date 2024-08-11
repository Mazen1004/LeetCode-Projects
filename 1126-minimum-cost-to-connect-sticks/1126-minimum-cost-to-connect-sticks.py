class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        cost = 0
        heapq.heapify(sticks) #min heap
        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            cost = cost + first + second
            heapq.heappush(sticks, first + second)

        return cost

        