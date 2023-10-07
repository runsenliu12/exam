class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        mylist = list(s)
        counts = mylist.count("1")
        mylist[-1] = "1"
        i = 0
        while i < counts - 1:
            mylist[i] = "1"
            i = i + 1
        for j in range(i, len(mylist)):
            mylist[j] = "0"
        mylist[-1] = "1"
        return "".join(mylist)


if __name__ == "__main__":
    s = Solution()
    print(s.maximumOddBinaryNumber("010"))
    print(s.maximumOddBinaryNumber("0101"))
