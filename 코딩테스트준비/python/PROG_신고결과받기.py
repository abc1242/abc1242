id_list =["muzi", "frodo", "apeach", "neo"]
report =["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}
    #신고당한사람들 체크
    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        #신고횟수가 초과면
        if reports[r.split()[1]] >= k:
            #정지된 사람을 신고한 사람에게 +1
            answer[id_list.index(r.split()[0])] += 1    ##핵심

    return answer

print(solution(id_list,report,k))