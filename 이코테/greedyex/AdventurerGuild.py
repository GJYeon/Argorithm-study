N = int(input())
adventurer = list(map(int,input().split()))
adventurer.sort(reverse=True)
i = 1
count = 0
while(i<=N):
    n = adventurer[i-1]
    if(N < i+n -1):
        i += 1
    else:
        i += n
        count += 1
print(count)