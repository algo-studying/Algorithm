T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            sumV = 0
            for xi in range(M):
                for yj in range(M):
                    sumV += arr[i+xi][j+yj]
                if maxV < sumV:
                    maxV = sumV
    print(f'#{t} {maxV}')