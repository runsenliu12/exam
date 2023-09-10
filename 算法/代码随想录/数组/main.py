from typing import List


def specialArray(self, nums: List[int]) -> int:
    for i in range(len(nums)):
        ans = len([num  for num in  nums if num >= i])
        if ans == i:
            return i
    return -1