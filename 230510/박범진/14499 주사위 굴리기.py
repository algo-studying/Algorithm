from collections import deque

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

N, M, x, y, K = map(int, input().split())    # 변수를 좀 더 신경써서 짓자
arr = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

## 기본원리

# 1. 방향에 따라서 이동하고
# 2. deque(rotate)로 주사위를 회전시키고
# 3. 조건에 맞춰서 값을 넣은후에 출력한다.

for direction in order:      # 주어진 방향을 전부 실행
    if direction == 1:       # 방향에 맞춰서
        if 0 <= x < N and 0 <= y + 1 < M:    # 지도 안에 있을 경우
            li = deque([a, c, f, d])
            li.rotate(-1)    # 주사위를 회전시키고
            result = list(li)
            a = result[0]
            c = result[1]
            f = result[2]
            d = result[3]
            y = y + 1
            if arr[x][y] == 0:    # 지도 좌표 값이 0이면
                arr[x][y] = a     # 지도 좌표 값은 주사위의 아래 부분의 값

            else:                 # 지도 좌표 값이 0이 아니면
                a = arr[x][y]     # 주사위 아래 부분은 지도 좌표의 값
                arr[x][y] = 0     # 그리고 지도의 좌표 값은 0이 됨
            print(f)              # 출력

        else:                     # 지도 안에 없으면 출력하지 않음
            continue

    elif direction == 2:
        if 0 <= x < N and 0 <= y - 1 < M:
            li = deque([a, c, f, d])
            li.rotate(1)
            result = list(li)
            a = result[0]
            c = result[1]
            f = result[2]
            d = result[3]
            y = y - 1
            if arr[x][y] == 0:
                arr[x][y] = a
            else:
                a = arr[x][y]
                arr[x][y] = 0
            print(f)
        else:
            continue

    elif direction == 3:
        if 0 <= x - 1 < N and 0 <= y < M:
            li = deque([a, e, f, b])
            li.rotate(1)
            result = list(li)
            a = result[0]
            e = result[1]
            f = result[2]
            b = result[3]
            x = x - 1

            if arr[x][y] == 0:
                arr[x][y] = a
            else:
                a = arr[x][y]
                arr[x][y] = 0
            print(f)
        else:
            continue

    elif direction == 4:
        if 0 <= x + 1 < N and 0 <= y < M:
            li = deque([a, e, f, b])
            li.rotate(-1)
            result = list(li)
            a = result[0]
            e = result[1]
            f = result[2]
            b = result[3]
            x = x + 1
            if arr[x][y] == 0:
                arr[x][y] = a
            else:
                a = arr[x][y]
                arr[x][y] = 0
            print(f)
        else:
            continue