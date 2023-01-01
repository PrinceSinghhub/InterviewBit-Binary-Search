class Solution:
	# @param A : list of list of integers
	# @return an integer
	def findMedian(self, A):

		arr = []

		for i in A:

			arr.extend(i)

		arr.sort()

		mid = len(arr) // 2

		return arr[mid]




ans = Solution()
arr = [
  [1, 3, 5],
  [2, 6, 9],
  [3, 6, 9]
]
print(ans.findMedian(arr))