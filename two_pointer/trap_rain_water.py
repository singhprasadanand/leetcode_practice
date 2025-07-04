"""
Problem: Trapping Rain Water (LeetCode 42)
https://leetcode.com/problems/trapping-rain-water/

Intuition:
The idea is to imagine water being trapped between the bars.
At each index, the amount of water trapped is determined by the minimum of
the highest bars to the left and right, minus the current bar height.

Sample:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6 units of water trapped.

Approach:
1. Precompute `left_max` and `right_max` arrays.
2. At each index, compute trapped water as:
   water = min(left_max[i], right_max[i]) - height[i]
3. Accumulate the result.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def trap_rainwater(inp:list[int])->int:
    n= len(inp)
    total_trapped = 0

    """
    Iterate at each level except first and last index
    """
    for i in range(1,n-1):
        """
        check maximum on left and maximum on right of current index
        """
        max_left = max(inp[:i])
        max_right = max(inp[1+1:])

        """
        water will get trapped till minimum level if compare between left or right of current index
        and once get the trapped level we need to deduct the current height of the index
        """
        total_trapped += min(max_left,max_right) - inp[i]

    return total_trapped


if __name__ == "__main__":
    inp = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap_rainwater(inp))