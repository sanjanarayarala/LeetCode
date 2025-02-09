class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low=0
        fast=len(height)-1
        total=0
        max_total=0
        while fast!=low:
            if min(height[low],height[fast])==height[low]:
                total= (fast-low)*min(height[low],height[fast])
                low+=1
                #print(low, fast, total)
            else:
                #print('fast-low', fast-low)
                #print('min(height[low],height[fast])', min(height[low],height[fast]))
                total= (fast-low)*min(height[low],height[fast])
                fast-=1
                #print(low, fast, total)
            
            if total>max_total:
                max_total=total

        return max_total