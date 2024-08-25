#주어진 숫자를 반으로 나누었을때 양쪽 합이 같은 경우를 구하기
N = input()
half = len(N)/2
sumfront = 0
sumback = 0
k= 0
for i in N:
    if(k < len(N)/2):
        sumfront += int(i)
    else:
        sumback += int(i)
    k+= 1
if(sumfront == sumback):
    print("LUCKY")
else:
    print("READY")