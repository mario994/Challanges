def solution(A, K):
    answer = ''
    if len(A) == 0 or len(A) == K:
        answer = A
    else:
        arr = A
        for x in range(K):
            valueMoved = arr.pop()
            arr.insert(0, valueMoved)
        answer = arr
    return answer