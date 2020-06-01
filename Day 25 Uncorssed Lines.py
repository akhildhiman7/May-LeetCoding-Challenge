
'''
We write the integers of A and B (in the order they are given) on two separate horizontal lines.
Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:
A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

Example 1:
Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:
Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:
Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2

Note:
1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000
'''

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        def helper(a, b, mx, i, j, m, n):
            if i == m or j == n:
                return 0
            if mx[i][j] != -1:
                return mx[i][j]

            aa, bb, cc = 0, 0, 0
            if a[i] == b[j]:
                aa = 1 + helper(a, b, mx, i+1, j+1, m, n)
            else:
                aa = helper(a, b, mx, i+1, j+1, m, n)

            bb = helper(a, b, mx, i+1, j, m, n)
            cc = helper(a, b, mx, i, j+1, m, n)

            mx[i][j] =  max(aa, bb, cc)

            return mx[i][j]

        len_a = len(A)
        len_b = len(B)
        if len_a == 0 or len_b == 0:
            return 0
        mx = [-1]*len_a

        for i in range(len_a):
            mx[i] = [-1]*len_b

        return helper(A, B, mx, 0, 0, len_a, len_b)
