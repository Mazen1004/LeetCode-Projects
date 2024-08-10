import heapq
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        currentsum = sum(nums)
        heap = [-num for num in nums]
        heapq.heapify(heap)

        ans = 0
        while target < currentsum:
            ans += 1
            x = heapq.heappop(heap)
            currentsum = currentsum - abs(x / 2)
            heapq.heappush(heap, x / 2)
        
        return ans