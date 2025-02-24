class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  

        if k == 0:
            return

        count = 0 
        start = 0  

        while count< n:
            current= start
            cur_val= nums[start]
            
            while True:
                next_idx = (current + k) % n
                nums[next_idx], cur_val = cur_val, nums[next_idx]
                current = next_idx
                count += 1
                
                if start == current:
                    break
            start += 1
        print(nums)