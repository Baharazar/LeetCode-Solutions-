class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            # If target is found, return the index
            if nums[i] == target:
                return i
            # If target should be inserted before the current number
            elif nums[i] > target:
                return i
        # If target is greater than all elements, it should be inserted at the end
        return len(nums)
