x = int(input())
y = int(input())
sum=0

for i in range(101):
    if x <= (i*i) and y>=(i*i):
        if sum==0:
            min = i*i
        sum += i*i

if sum ==0:
    print(-1)
else:
    print(sum)
    
    print(min)