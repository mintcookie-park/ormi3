def solution(l, r):
    
    mul = 1
    tmp = str(bin(mul))
    mul_to_bin = int(tmp[2:len(tmp)])
    answer =[]

    while mul_to_bin*5 <= r:
        
        if mul_to_bin*5 >= l:
            answer.append(mul_to_bin*5)
        
            
        mul += 1
        tmp = str(bin(mul))
        mul_to_bin = int(tmp[2:len(tmp)]) 


    return answer if len(answer) > 0 else [-1]