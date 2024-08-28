class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        while l < r:
            if nums[l] == nums[r] * (-1):
                return nums[r]
            if nums[l] * (-1) > nums[r] :
                l+=1
            elif nums[l] * (-1) < nums[r]:
                r-=1
        else:
            return -1
