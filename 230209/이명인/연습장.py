T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 0, 1, 1, -1, 0, 1, -1]        # 방향
    dc = [1, 1, 1, 0, -1, -1, -1, 0] 
    ans = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            v = arr[i][j]
            cnt = 0
            for d in range(8):
                newr = i + dr[d]
                newc = j + dc[d]

                if 0 <= newr < N and 0 <= newc < M:
                    t = arr[newr][newc]
                    if v > t:
                        cnt += 1

            if cnt >= 4:
                ans += 1
    print(ans) 
                      


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            sumV = 0
            for x in range(M):
                for y in range(M):
                    sumV += arr[i+x][i+y]
                if maxV < sumV:
                    maxV = sumV

    print(maxV)