def solution(absolutes, signs):
    answer = 0
    i = 0

    while i < len(signs):

        if signs[i] == False:
            absolutes[i] *= -1

        answer += absolutes[i]
        i += 1

    return answer