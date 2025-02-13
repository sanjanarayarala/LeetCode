class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l=[[] for _ in range(numRows)]
        j=0
        flag=0
        while True:
            i=0
            while i<=numRows-1:
                if j==len(s):
                    flag=1 
                    break
                l[i].append(s[j])
                j+=1
                i+=1
            if flag==1:
                break
            i=numRows-2
            while i>=1:
                if j==len(s):
                    flag=1 
                    break
                l[i].append(s[j])
                j+=1
                i-=1
            if flag==1:
                break
        o=""
        for i in l:
            for j in i:
                o+=j
    
        return o