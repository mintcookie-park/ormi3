def solution(board):
    answer = 0
    dp=[[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    
    dp[0] = board[0]
    for row in range(len(board)):
        dp[row][0] = board[row][0]

    for row in range(0,len(dp)):
        for col in range(0,len(dp[0])):
            if (row - 1 >= 0) and (col -1 >= 0) and board[row][col] ==1:
            	
                dp[row][col] = min(dp[row][col-1],dp[row-1][col],dp[row-1][col-1])+1

    for i in range(len(dp)):
        temp = max(dp[i])
        answer = max(answer, temp)

    return answer*answer