def solution(string: str) -> bool:
#    squeezed = ''.join(filter(str.isalpha, string)).lower() # Only alphabets
    squeezed = ''.join(filter(str.isalnum, string)).lower() # Alphabets + numbers
    print(squeezed)
    for i in range(len(squeezed)//2):
        compareWith = len(squeezed) - i - 1
        if i == compareWith: break
        if squeezed[i] != squeezed[compareWith]:
            return False
    return True

print(solution("1race a car"))#False
print(solution("1A man, a plan, a canal: Panama1"))#True
