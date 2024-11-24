class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        numcount = {}

        for num in nums1:  # Iterate through the elements of nums1
            if num in numcount:  # Check if the number is already in the dictionary
                numcount[num] += 1  # Increment the count
            else:
                numcount[num] = 1  # Initialize the count to 1

        result = []
        for num in nums2:
            if num in numcount and numcount[num] > 0:
                result.append(num)
                numcount[num] -= 1

        print(numcount)
        return result
            