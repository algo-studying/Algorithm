
def bfs(st, gole):
    Q = []
    visited = [[0]*16 for _ in range(16)]
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
            if 0 <= newr < 16 and 0 <= newc < 16 and arr[newr][newc] != 1 and not visited[newr][newc]:   
                Q.append((newr,newc))
                visited[newr][newc] = visited[vs][vg] + 1
    return 0
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                s = i
                g = j
                break

    print(f'#{tc} {bfs(s, g)}')
