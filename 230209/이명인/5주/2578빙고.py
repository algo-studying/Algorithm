def check(v):
    for m in range(N):
        for n in range(M):
            t = bingo[m][n]
            if t == v:
                # visited[][j] == 1

                # 2. 좌표를 벙문표시한다.
                visited[m][n] = 1

# 입력 없이 cnt return
def isBingo():
    # 3-1 가로 5줄 검사
    cnt = 0
    maxV = 0

    for i in range(N):
        sum1 = 0
        for j in range(N):
            sum1 += visited[i][j]
        if sum1 == 5:
            cnt += 1

    # 3-2 세로 5중 검사
    for i in range(N):
        sum2 = 0
        for j in range(M):
            sum2 += visited[j][i]
            
        if sum2 == 5:
            cnt += 1       

    # 3-3 오른쪽 대각선
    sum3 = 0
    for i in range(N):
        sum3 += visited[i][i]              
    if sum3 == 5:
        cnt += 1

    # 3-4 왼쪽 대각선
    sum4 = 0
    for i in range(N):
        sum4 += visited[i][N-i-1]   
    if sum4 == 5:
        cnt += 1

    return cnt


N, M = 5, 5
bingo = [list(map(int, input().split())) for _ in range(N)]
mc = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt2 = 0
s = 0
for i in range(N):
    for j in range(M):
        v = mc[i][j]
        
        cnt2 += 1
        # print(v, cnt2)
        #1. bingo 에서 좌표를 찾는다.
        check(v)
        # print(visited)
        
        #3. 빙고인지 확인다.
        
        cnt = isBingo()
        if cnt >= 3:
           print(cnt2)
           break
    if cnt >= 3:
        break