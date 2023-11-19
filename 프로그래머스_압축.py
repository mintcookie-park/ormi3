def solution(msg):
    alpha_dict = {chr(65+i) : i+1 for i in range(26)}
    
    i = 0
    check = ''
    result = []
    num = 27
    
    while i < len(msg):
        check += msg[i]
        if check in alpha_dict:
            i+=1
        else:
            alpha_dict[check] = num
            num += 1
            result.append(alpha_dict[check[:-1]])
            check = ''
    result.append(alpha_dict[check])
    return result