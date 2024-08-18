N = int(input())
warehouse = list(map(int,input().split()))
d = [0]*30001
d[1] = warehouse[0]
d[2] = warehouse[1]
d[3] = d[1] + warehouse[2]
for i in range(4,N+1):
    d[i] = max(d[i-2],d[i-3]) + warehouse[i-1]

print(d[N])