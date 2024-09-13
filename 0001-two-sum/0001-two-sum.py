class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the value and its corresponding index
        num_to_index = {}

        # Loop through the array to find the complement that adds up to the target
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                # If complement exists in the dictionary, return the two indices
                return [num_to_index[complement], i]
            # Store the current number and its index
            num_to_index[num] = i

        # Return empty if no solution is found (though the problem guarantees one)
        return []



