class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        h = 0
        Max = 0
        Min = 0
        ans = 0

        for i in range(len(A)):
            Max = max(Max, A[i])

        while Min <= Max:

            mid = Min + (Max - Min) // 2

            wood = 0
            for i in range(len(A)):
                if A[i] - mid > 0:
                    wood = wood + A[i] - mid

            if wood >= B:
                Min = mid + 1
                ans = max(ans, mid)

            else:
                Max = mid - 1

        return ans


ans = Solution()
A = [20, 15, 10, 17]
B = 7
print(ans.solve(A,B))