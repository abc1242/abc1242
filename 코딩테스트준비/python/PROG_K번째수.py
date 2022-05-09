def solution(array, commands):
    answer = []
    for cmd in commands:
        i = cmd[0] -1
        j = cmd[1]
        k = cmd[2] -1

        tmp = array[i:j]
        tmp.sort()
        answer.append(tmp[k])

    return answer

array =[1, 5, 2, 6, 3, 7, 4]
commands =[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution(array,commands)
