class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        max=1
        major=max
        element=nums[0]
        i=1
        while i<len(nums):
            if nums[i]==nums[i-1]:
                max+=1
                i+=1
                if i==len(nums):
                    print('hi')
                    if max>major:
                        major=max
                        element=nums[i-1]
                        print(element)
            else:
                if max>major:
                    major=max
                    element=nums[i-1]
                    print(element)
                max=1
                i+=1
        
        return element