class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        # also use two line on code
        # Max = max(arr)
        # return Max

        copy = A.copy()
        copy.sort()

        if A == copy:
            return A[-1]

        if A == copy[::-1]:
            return A[0]

        for i in range(1, len(A) - 1):

            if A[i] > A[i - 1] and A[i] > A[i + 1]:
                return A[i]


ans = Solution()
arr = [10, 9, 8, 70, 6,1, 2, 3, 4, 5]
print(ans.solve(arr))