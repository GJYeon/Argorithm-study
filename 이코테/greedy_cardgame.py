N, M = map(int, input().split())
Min = 0
for i in range(N):
    minnum = min(list(map(int, input().split())))   #주어진 행의 최소값을 이용 >> 그리디
    if(Min < minnum):  #행의 최소값 중의 최대값을 구한다.
        Min = minnum
print(Min)