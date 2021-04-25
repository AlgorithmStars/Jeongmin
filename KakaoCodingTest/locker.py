import numpy as np

def solution(key, locker):
    key = np.array(key)
    M = len(key)
    locker = np.array(locker)
    N = len(locker)

    bigLocker = np.zeros((2*M+N, 2*M+N))
    bigLocker[M:M+N,M:M+N] = locker
    for _ in range(4):
        for i in range(len(bigLocker) - M):
            for j in range(len(bigLocker[0]) - M):
                bigLocker[i:i+M, j:j+M] += key
                if isLocked(bigLocker[M:M+N, M:M+N]):
                    return True
                bigLocker[i:i+M, j:j+M] -= key

        key = key.T
        key = np.flip(key, axis=1)
    return False

def isLocked(bigLocker):
    for i in range(len(bigLocker)):
        for j in range(len(bigLocker[0])):
            if bigLocker[i][j] != 1:
                return False
    return True


k = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
l = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(k, l))
