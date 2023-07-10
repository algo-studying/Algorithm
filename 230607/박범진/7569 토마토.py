from collections import deque
from sys import stdin
input = stdin.readline


def BFS():
    global answer
    while queue:
        ci, cj, ck = queue.popleft()
        for di, dj, dk in [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (-1, 0, 0), (1, 0, 0)]:
            ni, nj, nk = ci+di, cj+dj, ck+dk
            if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and arr[ni][nj][nk] == 0 and not visited[ni][nj][nk]:
                queue.append((ni, nj, nk))
                visited[ni][nj][nk] = True
                arr[ni][nj][nk] = arr[ci][cj][ck] + 1
                answer = arr[ci][cj][ck]


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]
queue = deque()
answer = -1000

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1 and not visited[i][j][k]:
                visited[i][j][k] = True
                queue.append((i, j, k))    # queue를 bfs 밖에서 넣어준 다음 bfs를 실행시켜도 된다는 사실을 알았다.
BFS()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                print(-1)
                exit()
            elif arr[i][j][k] > answer:
                answer = arr[i][j][k]

print(answer-1)