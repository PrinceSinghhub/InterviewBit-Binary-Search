class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        low = 0
        high = len(A) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if B == A[mid]:
                return mid
            elif A[mid] <= A[high]:
                if (B > A[mid]) & (B <= A[high]):
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if (A[low] <= B) & (B < A[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
        return -1


# using Function
class Solution:

    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        if B in A:
            return A.index(B)
        return -1
