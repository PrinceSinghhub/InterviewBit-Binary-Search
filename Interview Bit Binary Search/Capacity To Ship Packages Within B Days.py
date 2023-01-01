class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, weights, D):

        def feasible(capacity):
            days = 1
            local = 0
            for w in weights:
                local += w
                if local > capacity:
                    local = w
                    days += 1
                    if days > D:
                        return False
            return True

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left

ans = Solution()
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = 5
print(ans.solve(A,B))