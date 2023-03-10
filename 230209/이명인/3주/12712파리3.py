T = int(input())
 
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0
    for r in range(N):
        for c in range(N):
            fly = arr[r][c]
            for k in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                for mul in range(1, M):
                    nr = r + k[0] * mul
                    nc = c + k[1] * mul
                    if 0 <= nr < N and 0 <= nc < N:
                        fly += arr[nr][nc]
                    else:
                        break
                if maxV < fly:
                    maxV = fly
            fly = arr[r][c]
            for k in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                for mul in range(1, M):
                    nr = r + k[0] * mul
                    nc = c + k[1] * mul
                    if 0 <= nr < N and 0 <= nc < N:
                        fly += arr[nr][nc]
                    else:
                        break
                if maxV < fly:
                    maxV = fly
 
    print(f'#{tc} {maxV}')