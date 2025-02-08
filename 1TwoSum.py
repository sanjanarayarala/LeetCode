def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[]
        nums2=nums[:]
        nums.sort()
        low=0
        high=len(nums)-1
        for i in range(len(nums)):
            total= nums[low]+nums[high]
            if total==target:
                break
            elif total>target:
                high-=1
            elif total<target:
                low+=1

        for i in range(len(nums2)):
            if nums[low]==nums2[i] or nums[high]==nums2[i]:
                res.append(i)

        return res