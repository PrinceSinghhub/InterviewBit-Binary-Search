class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):

        for i in A:
            if B in i:
                return 1
        return 0

# todo optimize Code
'''
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        t=[]
        n=len(A)
        for i in range(n):
            t.extend(A[0])
            del A[0]
        if B in t:
            return 1
        return 0
        
        nrow=len(A)
        ncol=len(A[0])
        left=0
        right=nrow*ncol-1
        while left<=right:
            mid=(right+left)//2
            ci,cj=(mid//ncol,mid%ncol)
            if B>A[ci][cj]:
                left=mid+1
            elif B<A[ci][cj]:
                right=mid-1
            else:
                return 1
        return 0
        '''
