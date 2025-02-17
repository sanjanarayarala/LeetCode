class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        first=colors[0]
        last=colors[len(colors)-1]
        max_dist=0
        dist=0
        for i in range(1, len(colors)):
            if first!=colors[i]:
                dist=abs(0-i)
                if(dist>max_dist):
                    max_dist=dist

        for i in range(len(colors)-1, -1, -1):
            if last!=colors[i]:
                dist=abs(len(colors)-1-i)
                if(dist>max_dist):
                    max_dist=dist

        return max_dist