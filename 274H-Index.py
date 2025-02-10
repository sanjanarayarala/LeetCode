class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        sorted_cit=sorted(citations)
        
        citations.sort()  
        n= len(citations)

        for i in range(n):
            h= n-i  
            if citations[i]>= h:
                return h

        return 0 