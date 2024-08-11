import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #pop elements most distance from origin using max-heap
        heap = []
        origin = [0,0]

        for point in points:
            distance = math.dist(point, origin)
            heapq.heappush(heap, (-distance, point))
            if len(heap) > k:
                heapq.heappop(heap)

        return [point[1] for point in heap]