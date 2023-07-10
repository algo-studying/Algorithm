def solution(record):
    # {유저 아이디 :  닉네임}의 형식으로 저장
    dict = {}

    # 행동과 유저 아이디를 리스트로 저장
    result = []

    # 정답
    answer = []

    for sentence in record:
        # 행동, 유저 아이디, 닉네임을 구분하기위해 나눔
        lst = list(sentence.split())

        # Leave일 때
        if len(lst) == 2:
            result.append(['Leave', lst[1]])
        # Enter나 Change일 때
        else:
            if lst[0] == 'Enter':
                dict[lst[1]] = lst[2]
                result.append(['Enter', lst[1]])
            else:
                dict[lst[1]] = lst[2]

    for order in result:
        if order[0] == 'Enter':
            answer.append(f"{dict[order[1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{dict[order[1]]}님이 나갔습니다.")

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))