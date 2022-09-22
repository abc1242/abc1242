import math
def solution(fees, records):
    answer = []
    
    base_time, base_fee, add_time, add_fee = fees
    
    
    parking = dict()
    result = dict()
    for r in records:
        
        time, number, inout = r.split(' ')
        
        if inout == 'IN':

            parking[number] = time
        else:
            
            in_h, in_m = map(int,parking[number].split(':'))
            
            out_h, out_m = map(int, time.split(':') )
            
        
            total = (out_h - in_h) * 60 + out_m - in_m
            
            if number not in result.keys():
                result[number] = total
            else:
                result[number] += total
            
            parking.pop(number)
    
    
    for last_number in parking.keys():

            in_h, in_m = map(int,parking[last_number].split(':'))
            
            out_h, out_m = 23,59
            
        
            total = (out_h - in_h) * 60 + out_m - in_m
            
            if last_number not in result.keys():
                result[last_number] = total
            else:
                result[last_number] += total

    for n, t in sorted(result.items()):


            f = 0
            if t <= base_time:
                f = base_fee
            else:
                f = base_fee
                t -= base_time

                f += math.ceil(t/add_time) * add_fee

            answer.append(f)
        
        
    return answer