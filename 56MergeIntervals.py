def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        low=0
        high=0
        l=[]
        i=1
        while i<=len(intervals)-1:
            if intervals[low][0]<=intervals[i][0] and intervals[i][0]<=intervals[high][1]:
                if intervals[high][1]<intervals[i][1]:
                    high=i
                else:
                    pass
                i+=1
            else:
                n=[]
                n.append(intervals[low][0])
                n.append(intervals[high][1])
                l.append(n)
                low=i
                high=i
                i+=1
        n=[]
        n.append(intervals[low][0])
        n.append(intervals[high][1])
        l.append(n)     
        return l