class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        high= len(nums)-1
        mid= (low+high)//2
        if nums[low]<nums[high]:
            return nums[low]
        while low!=high:
            if nums[mid]<nums[high]:
                high=mid
                mid= (low+high)//2
            else:
                low=mid+1
                mid=(low+high)//2
                
        return nums[low]
        