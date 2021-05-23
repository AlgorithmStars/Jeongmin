from collections import defaultdict

def solution(n, weak, dist):
    def nextWeakPoint(index):
        return 0 if index == len(weak) - 1 else index + 1
    def generateDistancePairs():
        distOfPair = defaultdict(list)
        for start in range(len(weak)):
            end = nextWeakPoint(start) 

            while start != end:
                distToNext = weak[end] - weak[start]
                if distToNext < 0:
                    distToNext += n
                if distToNext <= dist[-1]:
                    distOfPair[distToNext].append((start, end))
                end = nextWeakPoint(end)
        return distOfPair


    def sliceCircle(circle, start, end):
        if start == end:
            return []
        if start > end:
            circle = circle[:start]
            circle = circle[end+1:]
        else:
            circle = circle[:start] + circle[end+1:]
        return circle

    def matchCounter(distOfPair, circle, friends):
        if len(circle) == 0:
            return 0
        if len(friends) == 0:
            return -1

        friendCap = friends.pop() + 1
        pairs = None

        while pairs is None:
            friendCap -= 1
            pairs = distOfPair.get(friendCap)

        result = 201 # MAX
        for pair in pairs:
            start, end = pair
            remainder = sliceCircle(circle, start, end)
            result = min(matchCounter(distOfPair, remainder, friends.copy()) + 1, result)
        return result

    # dist.sort()
    distOfPair = generateDistancePairs()
    print([(k,distOfPair[k]) for k in sorted(distOfPair.keys(), reverse=True)])
    return matchCounter(distOfPair, weak, dist)

print(solution(12, [1,5,6,10], [1,2,3,4]))
print()
print(solution(12, [1,3,4,9,10], [3,5,7]))
