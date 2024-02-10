def solution(my_string, m, c):
    answer = ''
    temp_list = []
    for i in range(len(my_string)//m):
        temp_list.append(list(my_string[i*m:i*m+m]))
        
    for i in temp_list:
        answer += i[c-1]
    return answer