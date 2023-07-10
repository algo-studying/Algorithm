today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

def solution(today, terms, privacies):
    today_yyyy, today_mm, today_dd = map(int, today.split('.'))

    terms_dict = {}

    answer = []

    # 1. terms_dict안에 약관 {'A' : 6} 이런식으로 저장
    for term in terms:
        term_key, term_value = map(str, term.split())
        terms_dict[term_key] = int(term_value)

    # 2. 정책과 index 하나씩 추출
    for index, privacy in enumerate(privacies):
        date, term = map(str, privacy.split())
        privacy_yyyy, privacy_mm, privacy_dd = map(int, date.split('.'))

        # 3. 유효일에서 하루 빼기(유효기간은 약정 더한기간에서 하루 전이니까)
        privacy_dd -= 1

        # 4. 만약 유효일이 1일이었다면
        if privacy_dd == 0:
            privacy_dd = 28
            privacy_mm -= 1

        # 5. 만약 유효달이 1월이었다면
        if privacy_mm == 0:
            privacy_mm = 12
            privacy_yyyy -= 1

        # 6. 유효달 만큼 더하기
        privacy_mm += terms_dict[term]

        # 7. 12월보다 크다면
        if privacy_mm > 12:
            if privacy_mm % 12 != 0:
                privacy_yyyy += privacy_mm // 12
                privacy_mm %= 12
            else:
                privacy_yyyy += (privacy_mm - 12) // 12
                privacy_mm = 12

        # 8. 연도비교
        if today_yyyy > privacy_yyyy:
            answer.append(index+1)
            continue
        elif today_yyyy == privacy_yyyy:
            if today_mm > privacy_mm:
                answer.append((index+1))
                continue
            elif today_mm == privacy_mm:
                if today_dd > privacy_dd:
                    answer.append((index+1))
                    continue
                else:
                    continue
            else:
                continue
        else:
            continue

    return answer

print(solution(today, terms, privacies))