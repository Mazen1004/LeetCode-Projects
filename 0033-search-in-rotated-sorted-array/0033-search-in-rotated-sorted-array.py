class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <=r:
            m = (l+r)//2

            if nums[m] == target:
                return m

            print("nums m is: ", nums[m])

            if nums[l] <= nums[m]: #left side is sorted
                if nums[l] <= target <= nums[m]:
                    r = m -1 #target in first half
                else:
                    l =  m + 1 #target in second half
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1




            
        