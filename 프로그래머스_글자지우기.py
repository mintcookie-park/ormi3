def solution(my_string, indices):
    answer = ""
    index_set = set(indices)

    for i in range(len(my_string)):
        if i not in index_set:
            answer += my_string[i]

    return answer
