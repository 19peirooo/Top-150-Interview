# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

class Solution(object):
    def majorityElement(self, nums):
        count = 0
        maj = 0

        for num in nums:
            if count == 0:
                maj = num
            
            if maj == num:
                count += 1
            else:
                count -= 1
        
        return maj
        