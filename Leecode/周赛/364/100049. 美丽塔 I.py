from typing import List


class Solution:
    def get_sum_res(self, maxHeights):
        left = []
        # [6, 5, 5, 2, 1, 5, 5, 3, 6]
        for i in range(len(maxHeights) - 1):
            if i > 0 and maxHeights[i + 1] < left[-1]:
                left[-1] = maxHeights[i + 1]
            if maxHeights[i] >= maxHeights[i + 1]:
                left.append(maxHeights[i + 1])
            else:
                left.append(maxHeights[i])
            print(left)
        return left

    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        maxindex = maxHeights.index(max(maxHeights))
        print(maxindex)
        left = self.get_sum_res(maxHeights[: (maxindex + 1)])
        print(maxHeights[(maxindex):][::-1])  # [6, 5, 5, 2, 1, 5, 5, 3, 6]
        right = self.get_sum_res(maxHeights[(maxindex):][::-1])
        print(left)
        print(right)
        return sum(left) + maxHeights[maxindex] + sum(right)


if __name__ == "__main__":
    s = Solution()

    print(s.maximumSumOfHeights(maxHeights=[3, 6, 3, 5, 5, 1, 2, 5, 5, 6]))
