class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        myset = []
        maxlen = 0
        for end in range(len(s)):
            myset.append(s[end])
            while len(myset) > len(set(myset)):
                myset.remove(s[start])
                start += 1
            maxlen = max(maxlen, end - start + 1)
        return maxlen


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("bbbbb"))
