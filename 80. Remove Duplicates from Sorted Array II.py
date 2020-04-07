class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, count = 1, 1

        # Start from the second element of the array and process
        # elements one by one.
        while i < len(nums):

            if nums[i] == nums[i - 1]:
                count += 1

                if count > 2:
                    nums.pop(i)

                    # If we pop one, we need to shrink the index!
                    i -= 1
            else:

                count = 1

            # Move on to the next element in the array
            i += 1

        return len(nums)








