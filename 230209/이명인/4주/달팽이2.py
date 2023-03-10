# N = int(input())
# M = int(input())
# arr = [[0] * N for _ in range(N)]
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
# row = 0
# col = 0
# d = 0
# for num in range(1, N*N+1):
#     arr[row][col] = num

#     newr = row + dr[d]
#     newc = col + dc[d]
#     if newr < 0 or newr >= N or newc < 0 or newc >= N or arr[newr][newc]!= 0:
#         d += 1
#         if d == 4:
#             d = 0
#     row = row + dr[d]
#     col = col + dc[d]

# for arri in arr:
#     print(*arri)





N = int(input())
M = int(input())
arr = [[0] * N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 시작좌표 
row, col = (N-1)//2, (N-1)//2
# 가운데 친구 1
arr[row][col] = 1

num = 2
size = 3

while row != 0 or col != 0:
    while num <= size * size:
        if row == col == (N - 1) // 2: # 시작점이면 cnt 세팅, 한 칸 위로
            cnt_up, cnt_down, cnt_left, cnt_right = size, size - 1, size - 1, size - 2
            row += dr[0]
            col += dc[0]
            cnt_up -= 1

        elif cnt_right > 0: # 우
            row += dr[3]
            col += dc[3]
            cnt_right -= 1

        elif cnt_down > 0: # 하
            row += dr[1]
            col += dc[1]
            cnt_down -= 1

        elif cnt_left > 0: # 좌
            row += dr[2]
            col += dc[2]
            cnt_left -= 1

        elif cnt_up > 0: # 상
            row += dr[0]
            col += dc[0]
            cnt_up -= 1

        arr[row][col] = num
        num += 1
        
    N -= 2
    size += 2

for j in range(len(arr)):
    print(*arr[j])
    if M in arr[j]:
        mrow = j + 1
        mcol = arr[j].index(M) + 1
print(mrow, mcol)


