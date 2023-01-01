import math


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        no_days_min = 0
        no_days_max = float('-inf')
        n = len(A)
        a = []

        for i in A:
            no_days_max = max(no_days_max, i[0], i[1], -i[0], -i[1])
            a.append(complex(i[0], i[1]))

        def get_no_zones(r):
            c = 0

            for i in range(n):
                for j in range(i + 1, n):
                    g = a[j] - a[i]
                    dist = abs(g)
                    if dist > 2 * r:
                        continue
                    mid = (a[i] + a[j]) / 2
                    h = (r ** 2 - (dist / 2) ** 2) ** 0.5
                    per = complex(-g.imag, g.real) * (h / dist)

                    c1 = c2 = 2
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        if abs(a[k] - (mid - per)) <= r:
                            c1 += 1
                        if abs(a[k] - (mid + per)) <= r:
                            c2 += 1

                    c = max(c, c1, c2)

            return c

        while no_days_min < no_days_max:
            no_days_mid = (no_days_min + no_days_max) // 2

            no_zones = get_no_zones(no_days_mid)
            # print("*", no_days_mid, no_zones)

            if no_zones >= B:
                no_days_max = no_days_mid
            else:
                no_days_min = no_days_mid + 1
            # print(no_days_min, no_days_max)

        return no_days_max




