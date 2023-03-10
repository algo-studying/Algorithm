T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [-1, 0, 1, 1, -1, 0, 1, -1]        # 방향
    dc = [1, 1, 1, 0, -1, -1, -1, 0]    
    cnt2 = 0                                # 4방향이 숫자가 큰걸 카운트
    for i in range(len(arr)):               
        for j in range(len(arr[i])):        
            v = arr[i][j]                   
            cnt = 0                         # 인접한 곳이 숫자가 큰걸 카운트
            for d in range(8):              
                newr = i + dr[d]            
                newc = j + dc[d]            

                if 0 <= newr < N and 0 <= newc < M:
                    t = arr[newr][newc]     
                    if v > t:               # arr의 좌표를 통해 arr 값비교
                        cnt += 1            
            if cnt >= 4:                    # 4보다 크면 카운트
                cnt2 += 1

    print(f'#{tc} {cnt2}')