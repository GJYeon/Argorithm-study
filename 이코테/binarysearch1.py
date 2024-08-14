N = int(input())
product = list(map(int, input().split()))
product.sort()
M = int(input())
request = list(map(int, input().split()))
response = ['no']*3
for i in range(M):
    start = 0
    end = N-1
    while(start <= end):
        mid = (start + end)//2
        if(product[mid] == request[i]):
            response[i] = 'yes'
            break
        elif(product[mid] < request[i]):
            start = mid + 1
            continue
        else:
            end = mid - 1
            continue

for i in range(M):
    print(response[i], end=' ')