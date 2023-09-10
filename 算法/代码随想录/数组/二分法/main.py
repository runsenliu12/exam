from typing import List


def answerQueries( nums: List[int], queries: List[int]) -> List[int]:
    sort_nums = sorted(nums)
    res = []
    for query in queries:
        j = 0
        count = 0
        while j <= len(sort_nums) - 1:
            if count >= query:
                break
            else:
                count += sort_nums[j]
            j += 1
        if count >  query:
            res.append(j -1 )
        else:
            res.append(j)

    return res

if __name__ == '__main__':
   print(    answerQueries(nums = [4, 5, 2, 1], queries = [3, 10, 21]))