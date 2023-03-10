T = int(input())
for t in range(1, T+1):
    N = int(input())
    brd = [[0] * 10 for _ in range(10)] # 얕은복사안하고 각각 따로 만들어줘

    for i in range(N):
        # s = list(map(int, input().split()))
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                # brd[r][c] = color
                # t = brd[r][c] + color
                brd[r][c] += color
        cnt = 0
        for r in range(10):
            for c in range(10):
                if brd[r][c] == 3:
                    cnt += 1
    print(f'#{t} {cnt}')