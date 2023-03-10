T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    row = 0
    col = 0
    d = 0
    for i in range(1, N*N+1):
        arr[row][col] = i

        newr = row + dr[d]
        newc = col + dc[d]
        if newr < 0 or newr >= N or newc < 0 or newc >= N or arr[newr][newc]!= 0:
            # d += 1
            # if d == 4:
            #     d = 0
            d = (d+1) % 4
        row = row + dr[d]
        col = col + dc[d]


    print(f'#{t}')
    for arri in arr:
        print(*arri)