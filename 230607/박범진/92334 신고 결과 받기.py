def solution(id_list, report, k):
    ans = {}       # { 신고 당한 사람(str) : 신고한 사람들(list) }의 구조로 딕셔너리를 만듬
    res = {}       # { 신고한 사람(str) : 신고 처리가 완료 되어 날아온 메세지의 수(int) }의 구조로 딕셔너리를 만듬
    answer = []    # 정답 출력용

    for id in id_list:    # 모든 유저들을 순서대로 위에서 정한 딕셔너리에 형식에 맞춰 집어 넣음
        ans[id] = []
        res[id] = 0

    for word in report:
        splitWord = word.split()    # [ 신고한 사람, 신고 당한 사람 ]의 구조로 나눔
        if splitWord[0] not in ans[splitWord[1]]:    # { 신고 당한 사람 : 신고한 사람들 }에서 신고한 사람들의 리스트에 포함되어 있지 않으면
            ans[splitWord[1]].append(splitWord[0])

    for id in id_list:
        if len(ans[id]) >= k:    # 신고 횟수가 정지 기준 보다 많으면
            for cnt in ans[id]:  # 신고한 사람들 한명씩 카운트를 1씩 더해줌
                res[cnt] += 1

    for id in id_list:           # 정답 출력 저장
        answer.append(res[id])

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
print(solution(id_list, report, k))

