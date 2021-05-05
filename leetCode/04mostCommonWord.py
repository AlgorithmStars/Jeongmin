import collections
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = re.sub(r'[^\w]', ' ', paragraph)
        words = words.lower().split()
        counter = collections.Counter(words)
        for ban in banned:
            counter.pop(ban, None)
        return counter.most_common(1)[0][0]


sol = Solution()
print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
