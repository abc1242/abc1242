from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = deque([0] * bridge_length)
    waiting = deque(truck_weights)
    
    sumb = sum(bridge)
    while waiting:
        answer+=1
        sumb -= bridge.popleft()
        if sumb + waiting[0] <= weight:
            sumb += waiting[0]
            bridge.append(waiting.popleft())
            
        else:
            bridge.append(0)
    cnt =0

    for i in list(bridge)[::-1]:
        cnt+=1
        if i !=0:
            answer += bridge_length - cnt+1
            break
    return answer