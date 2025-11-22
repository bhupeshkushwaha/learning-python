"""k_length_apart algorithm translated to Python.

Given an array of 0s and 1s and integers k, return True if there
are two 1s with distance at least k between them.
"""
from typing import List


def k_length_apart(nums: List[int], k: int) -> bool:
    last = -1
    for i, v in enumerate(nums):
        if v == 1:
            if last != -1 and i - last - 1 < k:
                return False
            last = i
    return True


if __name__ == "__main__":
    # Example
    print(k_length_apart([1,0,0,0,1,0,0,1], 2))  # True
