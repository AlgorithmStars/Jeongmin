def solution(p:str) -> str:
    if len(p) == 0:
        return p
    u,v = splitTwoWords(p)

    if u[0] == '(': 
        return u + solution(v)

    answer = '('
    answer += solution(v)
    answer += ')'
    substr = [')' if uu == '(' else '(' for uu in u[1:-1]]
    answer += ''.join(substr)
    return answer

def splitTwoWords(p:str) -> tuple[str, str]:
    first = p[0]
    stack = []
    for i in range(len(p)):
        pp = p[i]
        if first == pp:
            stack.append(pp)
        else:
            stack.pop()
        if len(stack) == 0:
            return p[:i+1], p[i+1:]
    return p, ''

word = "(()())()"
#word = ")("
word = "()))((()"
print(solution(word))
