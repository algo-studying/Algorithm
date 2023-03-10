T = int(input())
for testcase in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    lst = []
    # 가로탐색
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt +=1
            if j == M-1 or arr[i][j] == 0:
                lst.append(cnt)
                cnt= 0
    # 세로탐색
    for i in range(M):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt +=1
            if j == N-1 or arr[j][i] == 0:
                lst.append(cnt)
                cnt = 0
        
    print(f'#{testcase} {max(lst)}')








