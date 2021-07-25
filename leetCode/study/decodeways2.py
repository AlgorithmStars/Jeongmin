class Solution:
    def one(self, s:str) -> int:
        assert(len(s) == 1)
        if s == '0':
            return 0
        elif s == '*':
            return 9
        return 1

    def two(self, s:str) -> int:
        assert(len(s) == 2)

        def valid(s):
            if s[0] == '0':
                return False
            if '*' in s:
                if s[0] > '2':#not in ['1', '2', '*']:
                    return False
                return True
            if int(s) <= 26:
                return True
            return False

        if valid(s):
            if s == '**':
                return 15
            elif s[0] == '*':
                if s[1] <= '6':
                    return 2
                return 1
            elif s[1] == '*':
                if s[0] == '1':
                    return 9
                elif s[0] == '2':
                    return 6
                return 0
            else:
                return 1
        return 0

    
    def numDecodings(self, s:str) -> int:
        if len(s) == 1:
            return self.one(s)

        dp = [-1]*(len(s) + 1)
        dp[0] = 1
        dp[1] = self.one(s[0])

        for i in range(2, len(dp)):
            dp[i] = self.one(s[i-1]) * dp[i-1] +\
                    self.two(s[i-2:i]) * dp[i-2]
            dp[i] = dp[i] % 1000000007
        return dp[-1]


sol = Solution()
#print(sol.numDecodings('**'))
print(sol.numDecodings('12**610'))
print()
#        
#print(sol.numDecodings('1*'))
#print()

#print(sol.numDecodings('2*'))
#print()
