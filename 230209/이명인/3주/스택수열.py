'''
스택에 입력받는 1~N까지 무작위로 중복없이 append, pop 하기
결론 스택을 비워라 append 는 + pop은 -로 출력하기
불가능하면 no로출력
조건 
1. 반드시 오름차순 
2. 같은정수는 안나옴
3. 수열을 못만들면 no출력
4. 순서대로 들어가야함 ?

나의 생각 
1. 4가 들어온다 스택에 ++++ ?
2. 다음 수가 더작으면 pop ?
3. 12345678을 만들고 pop을한다 ?
'''
stack = []          
ans = []            
count = 0           

T = int(input())
for i in range(1, T+1):
    a = int(input())
    stack.append(a)

    while len(stack) != T:
        if ans[] > count:
            count += 1




