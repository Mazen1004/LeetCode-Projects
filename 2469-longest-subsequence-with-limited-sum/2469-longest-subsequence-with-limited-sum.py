class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()

        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        for query in queries:
            #Binary search for each value in query
            left = 0
            right = len(prefix) - 1

            while left <= right:
                mid = (left + right) // 2

                
                if prefix[mid] <= query:
                    left = mid + 1
                else:
                    right = mid - 1

            ans.append(left)

        return ans 

        