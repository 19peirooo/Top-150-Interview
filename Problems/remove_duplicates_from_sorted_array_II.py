# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. 
# The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 
# More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.

class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        k = 2

        for i in range(1,n):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        
        return k