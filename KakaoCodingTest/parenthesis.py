def solution(p):
    if len(p) == 0:
        return p
    u,v = splitTwoWords(p)

    if isValidWord(u):
        return u + solution(v)

    answer = '('
    answer += solution(v)
    answer += ')'
    substr = list(u[1:-1])
    for i in range(len(substr)):
        if substr[i] == ')':
            substr[i] = '('
        else:
            substr[i] = ')'
    answer += ''.join(substr)
    return answer


def isValidWord(u):
    stack = []
    try:
        for uu in u:
            if uu == '(':
                stack.append(uu)
            else:
                stack.pop() #')'

    except IndexError:
        return False

    return True

def splitTwoWords(p):
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
