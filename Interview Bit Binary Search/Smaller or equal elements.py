class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = 0
        start = 0
        end = len(A)-1

        while start <= end:
            mid = start + (end-start) //2

            if A[mid] > B:
                end = mid-1
            else:
                ans = mid+1
                start = mid+1
        return ans


ans = Solution()
A = [1, 3, 4, 4, 6]
B = 5
print(ans.solve(A,B))