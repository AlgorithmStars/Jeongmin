class Solution:
    def groupAnagrams(self, strs:list[str]) -> list[list[str]]:
        anagrams = {} 
        for i, word in enumerate(strs):
            word = list(word)
            word.sort()
            letters = ''.join(word)
            if anagrams.get(letters) is None:
                anagrams[letters] = [i]
            else:
                anagrams[letters].append(i)
        
        result = []
        for items in anagrams.values():
            result.append([strs[i] for i in items])
        return result

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
