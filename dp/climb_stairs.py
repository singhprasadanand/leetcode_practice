"""
Problem: Climbing Stairs (LeetCode 70)
https://leetcode.com/problems/climbing-stairs/

Intuition:
You're climbing a staircase with `n` steps. You can take **1 or 2 steps at a time**.
How many **distinct ways** can you reach the top?

This is the same as the **Fibonacci sequence**:
- To reach step `i`, you can come from:
    - step `i-1` (by taking 1 step)
    - step `i-2` (by taking 2 steps)

So,
    ways(i) = ways(i-1) + ways(i-2)

Base Cases:
- ways(0) = 1 (do nothing)
- ways(1) = 1 (one step)

Time Complexity: O(n)
Space Complexity: O(n)
"""

def climb_stair(n:int)->int:
    if n ==0 or n==1:
        return 1

    dp = [0]*(n+1)

    dp[0] = 1
    dp[1] = 1

    """
    To reach any step we can count the step to reach n-1 step and n-2 step
    """
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[-1]

if __name__ == "__main__":
    print(climb_stair(5))
