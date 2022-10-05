from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    listen = defaultdict(int)
    cnt = defaultdict(list)
    for i in range(len(genres)):
        
        listen[genres[i]]+=plays[i]
        cnt[genres[i]].append(plays[i])
   
    listen = sorted(listen.items(), key = lambda x:x[1],reverse=True)

    for i in cnt:
        cnt[i].sort(reverse = True)
    print(cnt)
    for g,t in listen:
        
        if len(cnt[g]) >=2:
            tmp1 = cnt[g][0]
            tmp2 = cnt[g][1]
            

            
            
            answer.append(plays.index(tmp1))
            plays[plays.index(tmp1)] = 0
            answer.append(plays.index(tmp2))
        elif len(cnt[g]) ==1:
            tmp1 = cnt[g][0]

            
            answer.append(plays.index(tmp1))
        
    
    return answer