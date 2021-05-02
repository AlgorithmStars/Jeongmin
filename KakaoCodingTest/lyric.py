class Trie:
    def __init__(self, isEnd=False):
        self.isEnd = isEnd
        self.children = {} # string:tries
        self.nodesPassedBy = 0

    def insert(self, key):
        node = self
        for ch in key:
            node.nodesPassedBy += 1
            child = node.children.get(ch)
            if child is None:
                node.children[ch] = Trie()
            node = node.children[ch] 
        node.isEnd = True

    def findAndCount(self, prefix):
        node = self
        for ch in prefix:
            node = node.children.get(ch)
            if node is None: return 0 
        return node.nodesPassedBy

#    def printTrie(self):
#        print(self.children.keys(), self.isEnd)
#        for child, childTrie in self.children.items():
#            childTrie.printTrie()


def solution(words, queries):
    wordsByLength = {} # length:tries
    wordsByLengthReverse = {}

    for word in words:
        if not wordsByLength.get(len(word)):
            wordsByLength[len(word)] = Trie()
            wordsByLengthReverse[len(word)] = Trie()
        wordsByLength[len(word)].insert(word)
        wordsByLengthReverse[len(word)].insert(word[::-1])

    counter = []
    for q in queries:
        if '?'*len(q) == q:
            targetDict = wordsByLength.get(len(q))
            if targetDict is None:
                counter.append(0)
            else:
                counter.append(targetDict.nodesPassedBy)
            continue

        count = 0
        try:
            if q[0] != '?':
                substr = q.split('?')[0]
                count = wordsByLength[len(q)].findAndCount(substr)
            else:
                substr = q[::-1].split('?')[0]
                count = wordsByLengthReverse[len(q)].findAndCount(substr)
        except Exception:
            pass

        counter.append(count)
    return counter


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],\
        ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]))
