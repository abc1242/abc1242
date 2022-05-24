import collections


def solution(N, stages):
    answer = []

    stages.sort()

    cnt = collections.Counter(stages)
    idx_sum = 0
    dic = dict()
    for i in range(1, N + 1):
        if (len(stages) - idx_sum) == 0:
            dic[i] = 0
            continue
        x = cnt[i] / (len(stages) - idx_sum)
        idx_sum += cnt[i]
        dic[i] = x

    sdict = sorted(dic, key=lambda x: dic[x], reverse=True)
    answer += sdict
    return answer