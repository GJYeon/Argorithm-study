
N , M = map(int,input().split())
ball = list(map(int,input().split()))
count = 0
for i in range(N-1):
    for j in range(i+1,N):
        if(ball[i] != ball[j]):
            count += 1
print(count)