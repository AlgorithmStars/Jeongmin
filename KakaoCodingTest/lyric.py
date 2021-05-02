count = 0

class Trie:
    def __init__(self, isEnd=False):
        self.isEnd = isEnd
        self.children = {} # string:tries

    def insert(self, key):
        node = self
        for ch in key:
            child = node.children.get(ch)
            if child is None:
                node.children[ch] = Trie()
            node = node.children[ch] 
        node.isEnd = True

    def find(self, prefix):
        node = self
        for ch in prefix:
            node = node.children.get(ch)
            if node is None: break
        return node

    def countAllLeaves(self):
        global count
        if self.isEnd:
            count += 1

        for trie in self.children.values():
            trie.countAllLeaves()

#    def printTrie(self):
#        print(self.children.keys(), self.isEnd)
#        for child, childTrie in self.children.items():
#            childTrie.printTrie()


def solution(words, queries):
    global count 

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
        count = 0
        try:
            if q[0] != '?':
                substr = q.split('?')[0]
                target = wordsByLength[len(q)].find(substr)
                target.countAllLeaves()
            else:
                substr = q[::-1].split('?')[0]
                target = wordsByLengthReverse[len(q)].find(substr)
                target.countAllLeaves()
        except KeyError:
            pass
        except AttributeError:
            pass

        counter.append(count)
    return counter


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],\
        ["fro??", "????o", "fr???", "fro???", "pro?", "??????"]))
