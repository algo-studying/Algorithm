# 1. arr1과 arr2의 첫 번째 숫자를 뺀다.
# 3. 비트연산자 |를 써서 or 로 둘중의 하나가 숫자 1이면 채운다.
# 4. result에 한행씩 저장한다.
# 5. 이렇게 배열의 갯수 n번만큼 반복한다.
# 6. 다 돌고나면 원하는 보물지도를 얻을 수 있다.
# 7. 출력 형식에 맞춰서 출력한다.
import re

def solution(n, arr1, arr2):
    result = []
    answer = []
    for i in range(n):
    # 1. arr1과 arr2의 첫 번째 숫자를 뺀다.
        arr1_decimal = arr1[i]
        arr2_decimal = arr2[i]

    # 3. 비트연산자 |를 써서 or 로 둘중의 하나가 숫자 1이면 채운다.
        treasure_map = arr1_decimal | arr2_decimal

    # 추가. 이진법으로 바꿨을 때 길이가 n만큼 되지 못한다면 n만큼 늘리기
        treasure_map = format(treasure_map, f'0{n}b')

    # 4. result에 한행씩 저장한다.
        result.append(treasure_map)

    # 5. 이렇게 배열의 갯수 n번만큼 반복한다.
    # 6. 다 돌고나면 원하는 보물지도를 얻을 수 있다.

    # 7. 출력 형식에 맞춰서 출력한다.
    for num in result:
        num = re.sub('1', '#', num)
        num = re.sub('0', ' ', num)
        answer.append(num)

    return answer

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

print(solution(n, arr1, arr2))