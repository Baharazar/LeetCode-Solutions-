class Solution(object):
    def removeElement(self, nums, val):
        # Initialize a variable to keep track of the position for non-val elements
        k = 0

        # Iterate over each element in the nums array
        for i in range(len(nums)):
            # If the current element is not equal to the given value 'val'
            if nums[i] != val:
                # Place the element at the k-th position in the nums array
                nums[k] = nums[i]
                # Increment k to point to the next position for a non-val element
                k += 1
        
        # Return k, which is the count of elements not equal to val
        return k
  