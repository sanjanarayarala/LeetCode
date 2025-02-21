class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        high=0
        low=0
        k=0
        l=[]
        flag=0
        for i in range(len(nums)):
            if i==len(nums)-1:
                if high==low:
                    l.append(str(nums[i]))
                    break
                else:
                    l.append(str(nums[low])+"->"+str(nums[high]))
                    break
            if nums[i]+1==nums[i+1]:
                high=k+1
            else:
                if high==low:
                    l.append(str(nums[i]))
                    high=k+1
                    low=high
                    k+=1
                    continue
                else:
                    l.append(str(nums[low])+"->"+str(nums[high]))
                    high=k+1
                    low=high
            k+=1
        return l