#상하좌우로 움직임이 주어지면 도착지점의 좌표를 출력
def move(v):
    if(v == 'L'):
        x = 0
        y = -1
    elif(v == 'R'):
        x = 0
        y = 1
    elif(v == 'U'):
        x = -1
        y = 0
    elif(v == 'D'):
        x = 1
        y = 0
    if(a + x < 1 or a + x > N or b + y <0 or b + y > N):
        return (a,b)
    else:
        return (a+x,b+y)

N = int(input())
movement = input().split()
a = 1
b = 1
for i in movement:
    a,b = move(i)
print(a,b)

