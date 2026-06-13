class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarysearch(arr,target):
            n=len(arr)
            l,r=0,n-1
            while l<=r:
                mid=l+(r-l)//2
                if arr[mid]==target:
                    return True
                elif arr[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return False

        l=0
        r=len(matrix)-1
        
        while l<=r:
            mid = l+(r-l)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                return binarysearch(matrix[mid],target)
            elif target<matrix[mid][0]:
                r=mid-1
            else:
                l=mid+1
        return False