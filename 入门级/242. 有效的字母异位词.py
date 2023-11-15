class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        s_count = Counter(s)
        i_count = Counter(t)
        return s_count == i_count


if __name__ == "__main__":
    s = Solution()
    s.isAnagram(s="anagram", t="nagaram")
