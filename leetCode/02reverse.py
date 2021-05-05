
# returns a new copied list

def solution(charList:list[str])-> str:
    return ''.join(charList[::-1])

# without return

def solution2(charList:list[str])-> None:
    # pointer swap(Traditional way)
    for i in range(len(charList)//2):
        j = len(charList) -i-1
        charList[i], charList[j] = charList[j], charList[i]

def solution3(s:list[str]) -> None:
    # Pythonic way
    s.reverse()

#print(solution())
s=['h','e','l','l','o']
solution2(s)
print(s)
