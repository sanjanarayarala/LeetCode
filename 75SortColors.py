class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        new=[0] * len(nums)
        l=0
        m=len(nums)-1
        k=0
        for i in range(len(nums)):
            if nums[i]==0:
                new[l]=0 
                l+=1 
            elif nums[i]==2:
                new[m]=2
                m-=1
            else:
                pass
        
        while l+1<=m+1:
            new[l]=1 
            l+=1

        for i in range(len(new)):
            nums[i]=new[i]