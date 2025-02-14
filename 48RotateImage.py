class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        l=0
        r=n-1
        j=n//2
        for _ in range(j):
            for i in range(r-l):
                #left to right
                temp=matrix[l+i][r]
                matrix[l+i][r]=matrix[l][l+i]
                #top to bottom
                cur=temp
                temp=matrix[r][r-i]
                matrix[r][r-i]=cur
                #right to left
                cur=temp
                temp=matrix[r-i][l]
                matrix[r-i][l]=cur
                #bottom to top
                cur=temp
                temp=matrix[l][l+i]
                matrix[l][l+i]=cur
            l+=1
            r-=1