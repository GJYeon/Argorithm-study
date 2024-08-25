#주어진 숫자로 만들 수 없는 가장 작은 자연수 구하기
N = int(input())
coin = list(map(int,input().split()))
coin.sort()
target = 1
for x in coin:
    if( target < x):
        print(target)
        break
    target += x

