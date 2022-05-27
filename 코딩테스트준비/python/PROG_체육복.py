def solution(n, lost, reserve):
    answer = n

    arr = [1 for _ in range(n + 1)]

    for i in lost:
        arr[i] -= 1

    for i in reserve:
        arr[i] += 1

    for i in range(n + 1):
        if arr[i] == 0:
            if arr[i - 1] == 2:
                arr[i - 1] = 1
                arr[i] = 1
            elif i + 1 <= n and arr[i + 1] == 2:
                arr[i + 1] = 1
                arr[i] = 1

    for i in range(n + 1):
        if arr[i] == 0:
            answer -= 1

    return answer