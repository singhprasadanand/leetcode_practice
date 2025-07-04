"""
Problem: Container With Most Water (LeetCode 11)
https://leetcode.com/problems/container-with-most-water/

Intuition:
We need to find two lines that together with the x-axis form a container,
such that the container contains the most water.

Key idea:
- Area = width * height
- The height is limited by the shorter of the two lines.
- Use two pointers: left at 0, right at n - 1, move the pointer pointing to the shorter height.

Dry Run:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

⏱ Time Complexity: O(n)
📦 Space Complexity: O(1)
"""

def calculate_water_volume(inp:list[int])->int:
    left = 0
    right = len(inp)-1

    """
    start iterating from both ends as we have to calculate bigger volume 
    and calculate volume by formula:
    volume = min(inp[left],inp[right])*(right-left)
    now move index further which is shorter in length as we need to get bigger volume
    """
    max_volume = 0
    while left<right:
        volume = min(inp[left],inp[right])*(right-left)

        """
        check if current volume is greater than max_volume
        """
        if volume>max_volume:
            max_volume=volume

        """
        We will be incrementing/decrementing the index which is smaller as we have to calculate for 
        bigger volume
        
        """
        if inp[left]<=inp[right]:
            left+=1
        else:
            right-=1

    return max_volume

if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(calculate_water_volume(height))