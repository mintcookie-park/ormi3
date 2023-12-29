def check(answer):
    for x, y, stuff in answer:
        if stuff == 0: #기둥 체크
            #'바닥 위' or '보의 한쪽 끝 위' or '또 다른 기둥 위' 
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif stuff == 1: #보 체크
            #'한쪽 끝 부분이 기둥 위' or '양쪽 끝 부분이 다른 보와 동시 연결'
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, stuff, operation = build
        if operation == 1: # 설치
            answer.append([x, y, stuff])
            if not check(answer): answer.remove([x, y, stuff])
        elif operation == 0: # 삭제
            answer.remove([x, y, stuff])
            if not check(answer): answer.append([x, y, stuff])
    answer.sort()
    return answer