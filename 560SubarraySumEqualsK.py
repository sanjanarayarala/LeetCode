class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        res=0
        cursum=0
        prefixSums={0:1}

        for n in nums:
            cursum+=n
            diff=cursum-k

            res+=prefixSums.get(diff,0)
            prefixSums[cursum]=1+prefixSums.get(cursum,0)

        return res