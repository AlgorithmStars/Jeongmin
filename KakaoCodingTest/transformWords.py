from collections import deque

def possible(word, target):
    diffs = sum([w != t for w, t in zip(list(word), list(target))])
    return diffs == 1

def solution(begin, target, words):
    leastChange = {begin: 0}

    queue = deque([begin])
    visited = [begin]
    while queue:
        word = queue.popleft()
        for nextword in words:
            if nextword not in visited and possible(word, nextword):
                visited.append(nextword)
                queue.append(nextword)
                leastChange[nextword] = leastChange[word] + 1

    
    if leastChange.get(target):
        return leastChange[target]
    return 0

print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log"]))
