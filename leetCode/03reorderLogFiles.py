class Solution:
    def reorderLogFiles(self, logs: list[str])->list[str]:
        digits, letters = [],[]
        for log in logs:
            values = log.split()
            if int(ord(values[1][0])) < 58:
                digits.append(values)
            else:
                letters.append(values)
        letters = sorted(letters, key=lambda item: (item[1:], item[0]))
        # digit 도 중복이 있으면 순서대로 정렬이 되어야 한다.. 어떻게?ㅠ

        result = letters
        result.extend(digits)
        return [' '.join(r) for r in result]
sol = Solution()
#logs = ["dig3 8 1 5 1", "dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
#logs = ["1 n u", "r 527", "j 893", "6 14", "6 82"]
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]

print(sol.reorderLogFiles(logs))

