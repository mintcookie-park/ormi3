def solution(record):
    userinfo = {}
    answer = []

    for text in record:
        info = text.split(' ')
        if info[0] == 'Enter':
            userid, nickname = info[1], info[2]
            userinfo[userid] = nickname
        elif info[0] == 'Change':
            userid, nickname = info[1], info[2]
            userinfo[userid] = nickname
    
    for text in record:
        info = text.split(' ') 
        if info[0] == 'Enter':
            userid = info[1]
            nickname = userinfo[userid]
            answer.append(f'{nickname}님이 들어왔습니다.')
        elif info[0] == 'Leave':
            userid = info[1]
            nickname = userinfo[userid]
            answer.append(f'{nickname}님이 나갔습니다.')
    return answer