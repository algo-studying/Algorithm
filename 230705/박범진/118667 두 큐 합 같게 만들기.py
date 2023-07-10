from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    count = 0

    #  (queue두개의 길이를 합친것) * 2만큼 돌았을 때 목표 값이 나오지 않으면 원래상태로 돌아왔다는 뜻
    deque_len = (len(queue1) + len(queue2)) * 2
    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)

    # 목표 숫자가 정수가 아닐 때
    if (sum_queue1 + sum_queue2) % 2 != 0:
        return -1

    i = 0
    while i < deque_len:

    # queue1의 합이 queue2의 합보다 작을 때
        if sum_queue1 < sum_queue2:
            pop_num = queue2.popleft()
            queue1.append(pop_num)

    # 처음에는 sum(deque1)으로 풀었더니 시간 초과가 여러 개가 생김
    # 그래서 처음에 sum값을 구해놓고 거기서 빼고 더하는 식으로 문제를 해결
            sum_queue1 += pop_num
            sum_queue2 -= pop_num
            count += 1
            i += 1

    # queue2의 합이 queue1의 합보다 작을 때
        elif sum_queue1 > sum_queue2:
            pop_num = queue1.popleft()
            queue2.append(pop_num)
            sum_queue2 += pop_num
            sum_queue1 -= pop_num
            count += 1
            i += 1

    # queue1 과 queue2의 합이 같을 때
        else:
            return count

    # 다 돌았는데 목표값이 나오지 않은 경우
    return -1


queue1 = []
queue2 = []
print(solution(queue1, queue2))




