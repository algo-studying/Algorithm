N, M = map(int, input().split())
visited = [0] * N  # 탐사 여부 check
s = []  # 출력 내용

def solve(depth, N, M):
    if depth == M:               # 탈출 조건
        print(' '.join(map(str, s)))  # list를 str으로 합쳐 출력
        return
    for i in range(len(visited)):   # 탐사 check 하면서
        
        if not visited[i]:          # 탐사 안했다면
            visited[i] = 1          # 탐사 시작(중복 제거)
            s.append(i+1)           # 탐사 내용
            solve(depth+1, N, M)    # 깊이 우선 탐색
            
            visited[i] = 0          # 깊이 탐사 
            s.pop()                 # 탐사 내용 제거

solve(0, N, M)