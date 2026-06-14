class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = [] 
        top,bottom,left,right = 0,len(matrix),0,len(matrix[0])

        while top<bottom and left<right:

            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1

            for j in range(top,bottom):
                res.append(matrix[j][right-1])
            right-=1

            if not(left<right and top<bottom):
                break
                
            for z in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][z])
            bottom-=1

            for k in range(bottom-1,top-1,-1):
                res.append(matrix[k][left])
            left+=1

        return res
