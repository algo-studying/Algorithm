def bfs(st, gole):
    Q = []
    visited = [[0]*16 for _ in range()]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    Q.append((st, gole))
    visited[st][gole] = 1

    while Q:
        vs, vg = Q.pop(0)
        if arr[vs][vg] == 3:
                return 1
        for d in range(4):
            newr = vs + dr[d]
            newc = vg + dc[d]
            if 0 <= newR < 16 and 0 <= newC < 16 and arr[newR][newC] != 1 and not visited[newR][newC]:       
            Q.append((newr,newc))
            visited[newR][newC] = visited[vs][vg] + 1
    return 0
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                s = i
                g = j

    print(s, g)
    # print(f&apos;#{tc} {bfs(s, g)}&apos;)

; def bfs(srow,scol):
;     q = []
;     N = 16
;     visited = [[0]*(N) for _ in range(N)]
 
;     q.append((srow,scol))
;     visited[srow][scol] = 0
;     while q:
;         (vrow,vcol) = q.pop(0) #원래는 (vrow,vcol)인데 튜플로 들어옴
;         # for d in range(4):
;         #     newr = vrow +dr[d]
;         #     newc = vcol +dc[d]
;         for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
;             newr = vrow +dr
;             newc = vcol +dc
 
;             if 0<=newr<N and 0<=newc<N: #좌표가 유효한지
;                 if arr[newr][newc] == 3: #목표에 도달
;                     return 1
;                 if arr[newr][newc] == 0 and visited[newr][newc]==0:
;                     q.append((newr,newc))
;                     visited[newr][newc] = visited[vrow][vcol] + 1
;     return 0
 
 
; T = 10
; for tc in range(1,T+1):
;     N = int(input())
;     arr = [list(map(int,input())) for _ in range(16)]
;     for row in range(16):  #3과 2의 위치 찾기
;         for col in range(16):
;             if arr[row][col] == 2: #2의 위치 찾기
;                 row1, col1 = row, col
 
;     ans = bfs(row1,col1)
;     print(f'#{tc} {ans}')
