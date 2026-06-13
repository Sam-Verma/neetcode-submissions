class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row,col=len(matrix),len(matrix[0])
        l=0
        r=row*col-1
        
        while l<=r:
            mid = l+(r-l)//2
            ele=matrix[mid//col][mid%col]
            if ele==target:
                return True
            elif target<ele:
                r=mid-1
            else:
                l=mid+1
        return False