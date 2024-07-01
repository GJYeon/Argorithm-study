N, M, K = map(int, input().split()) #배열의 크기 N, 숫자가 더해지는 횟수 M, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번 초과X
numberarray = list(map(int,input().split()))
numberarray.sort(reverse=True)
sum = 0 #큰 수의 법칙에 따라 더해진 값
count = 0
for i in range(M):
    if(count == K):
        sum += numberarray[1]
        count = 0
    else:
        sum += numberarray[0]
        count += 1

print(sum)



