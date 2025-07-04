"""
Problem: Transpose Matrix (LeetCode 867)
https://leetcode.com/problems/transpose-matrix/

Intuition:
The **transpose** of a matrix is a new matrix whose rows are the columns of the original.

If:
Original[i][j] → Transpose[j][i]

Example:
Input:
[
  [1, 2, 3],
  [4, 5, 6]
]

Output:
[
  [1, 4],
  [2, 5],
  [3, 6]
]

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

def transpose_matrix(inp:list[list[int]])->list[list[int]]|None:
    if len(inp)<=0:
        return None

    return [[row[col_index] for row in inp]for col_index in range(len(inp[0]))]


if __name__ == "__main__":
    inp = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    print(transpose_matrix(inp))