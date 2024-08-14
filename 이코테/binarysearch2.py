N , M = map(int, input().split())
height = list(map(int , input().split()))
height.sort()
start = 0
end = height[N-1]

def searchMaxHight(start, end):
    tempM = 0
    if(start>end):
        return
    mid = (start + end) // 2
    for i in height:
        if(mid < i):
            tempM += (i - mid)
    if(tempM==M):
        return mid
    elif(tempM<M):
        return searchMaxHight(start, mid -1)
    else:
        return searchMaxHight(mid + 1, end)

print(searchMaxHight(start, end))

