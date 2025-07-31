# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

class Solution(object):
    def canJump(self,nums):
        n = len(nums)
        reach = 0

        for i in range(n):
            if i > reach:
                return False
            
            reach = max(reach,i+nums[i])

            if reach >= n-1:
                return True
        
        return False