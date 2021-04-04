# 1. 문자열을 제일 앞부터 정해진 길이대로 잘라.
# 최소 압축 문자열의 길이는?
# ex. "ababcdcdababcdcd" ->  "2ab2cd2ab2cd"

def solution(s):
    answer = 1000
    if len(s) < 3:
        return len(s)

    for i in range(1, int(len(s)/2)+1):
        count = len(s)
        memory = ""
        dup = 1
        for j in range(0, len(s), i):
            token = s[j:j+i]
            #print(token)
            if memory == token:
                count -= i
                dup += 1

            else:
                memory = token
                if dup > 1:
                    count += len(str(dup))
                    dup = 1

        if dup > 1:
            count += len(str(dup))

        #print(count)
        answer = min(count, answer)
    return answer

#print(solution("abcabcdede"))
print(solution("ababcdcdababcdcd"))
