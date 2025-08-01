# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.

class Solution(object):
    def rotate1(self, nums, k):
        n = len(nums)
        k = k % n
        def reverse(ini,fin):
            while ini < fin:
                nums[ini],nums[fin] = nums[fin],nums[ini]
                ini += 1
                fin -= 1

        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
    
    def rotate2(self,nums,k):
        n = len(nums)
        k = k % n
        return nums[-k:] + nums[:-k]
    
    def rotate3(self,nums,k):
        n = len(nums)
        k = k % n
        for i in range(k):
            x = nums.pop()
            nums.insert(0,x)