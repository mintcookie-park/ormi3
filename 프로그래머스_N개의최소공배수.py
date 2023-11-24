def solution(arr):
    answer = 0
    n = 1                           
    
    while True:
        answer = max(arr) * n
        result = True
        for num in arr:
            if answer % num != 0:   
                result = False
                break
        if result:
            break                   
        n += 1
        
    return answer