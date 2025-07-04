"""
Problem: Two Sum (LeetCode 1)
https://leetcode.com/problems/two-sum/

Intuition:
Given an array `nums` and a target value, return **indices** of the two numbers such that they **add up to the target**.

We use a **hashmap (dictionary)** to store the complement (`target - num`) as we iterate.

Example:
Input: nums = [2, 7, 11, 15], target = 9
→ 2 + 7 = 9 → return [(0, 1)]

Real-World Analogy:
You’re shopping with a gift card (target), and want to pick 2 items (nums[i]) that exactly sum to that value.

Time Complexity: O(n)
Space Complexity: O(n)
"""


def two_sum_array(inp: list[int], k: int) -> list[tuple | None]:
    pairs = []
    hashmap = {}

    for index, number in enumerate(inp):
        required = k - number
        if required in hashmap:
            pairs.extend([(j, index) for j in hashmap.get(required)])
        hashmap.setdefault(number, []).append(index)
    return pairs


if __name__ == "__main__":
    nums = [2, 7, 11, 15,2]
    target = 9
    print(two_sum_array(nums,target))
