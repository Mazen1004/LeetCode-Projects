class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #create max-heap, pop in a loop until you hit k
        nums = [-num for num in nums]
        heapq.heapify(nums)
        poptimes = 0

        while poptimes < k:
            value = heapq.heappop(nums) * -1
            poptimes += 1

        return value
        