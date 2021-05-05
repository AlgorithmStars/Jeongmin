class Solution:
    def findShortPalindromeIndex(self, s:str) -> tuple[int, int]:
        if len(s) == 1:
            return

        for start in range(len(s) - 2):
            if s[start] == s[start + 2]: #odd palindrome
                yield start, start + 2
            if s[start] == s[start + 1]: # even palindrome
                yield start, start + 1

        if s[len(s) - 2] == s[len(s) - 1]:
            yield len(s) - 2, len(s) - 1


    def longestPalindrome(self, s:str) -> str:
        palinGenerator = self.findShortPalindromeIndex(s)
       
        result = ""
        for start, end in palinGenerator:
            while (start >= 1 and end <= len(s) - 2) and (s[start -1] == s[end +1]):
                start -= 1
                end += 1
            result = max(result, s[start:end+1], key=len)

        return result if len(result) else s[0]

sol = Solution()
string = ["babad", "cbbd", "fff", "a", "ac"]
for s in string:
    print(sol.longestPalindrome(s))
