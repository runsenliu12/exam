class Solution:
    def isHappy(self, n: int) -> bool:
        count = set()
        while n > 1:
            res = [int(i) ** 2 for i in list(str(n))]
            n = sum(res)
            if n in count:
                return False
            else:
                count.add(n)
        if n == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print(s.isHappy(n=19))
    print(s.isHappy(n=7))
    print(s.isHappy(n=2))
