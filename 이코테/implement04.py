#dfs방식이 쓰인 구현 문제
N ,M = map(int,input().split())
loc_r , loc_c, d = map(int,input().split())
Map = list()
for i in range(M):
    Map.append(list(map(int,input().split())))
count = 1
def dir(d):
    if(d == 0):
        return (-1,0)
    elif(d == 1):
        return (0,1)
    elif(d == 2):
        return (1,0)
    else:
        return (0,-1)

def move(r,c,d):      #dfs방식으로 조사한다.
    global count
    Map[r][c] = 1
    if(d-1 != -1):
        d = d-1
        mov_r, mov_c = dir(d)
        if (0 <= r + mov_r < N and 0 <= c + mov_c < M and Map[r + mov_r][c + mov_c] == 0):
            count += 1
            move(r + mov_r, c + mov_c, d)
    else:
        d = 3
        mov_r,mov_c = dir(d)
        if(0<=r+mov_r<N and 0<=c+mov_c<M and Map[r+mov_r][c+mov_c] == 0):
            count += 1
            move(r+mov_r,c+mov_c,d)

    if (d - 1 != -1):
        d = d - 1
        mov_r, mov_c = dir(d)
        if (0 <= r + mov_r < N and 0 <= c + mov_c < M and Map[r + mov_r][c + mov_c] == 0):
            count += 1
            move(r + mov_r, c + mov_c, d)
    else:
        d = 3
        mov_r, mov_c = dir(d)
        if (0 <= r + mov_r < N and 0 <= c + mov_c < M and Map[r + mov_r][c + mov_c] == 0):
            count += 1
            move(r + mov_r, c + mov_c, d)

    if (d - 1 != -1):
        d = d - 1
        mov_r, mov_c = dir(d)
        if (0 <= r + mov_r < N and 0 <= c + mov_c < M and Map[r + mov_r][c + mov_c] == 0):
            count += 1
            move(r + mov_r, c + mov_c, d)
    else:
        d = 3
        mov_r, mov_c = dir(d)
        if (0 <= r + mov_r < N and 0 <= c + mov_c < M and Map[r + mov_r][c + mov_c] == 0):
            count += 1
            move(r + mov_r, c + mov_c, d)

    if (d - 1 != -1):
        d = d - 1
        mov_r, mov_c = dir(d)
        if (0 <= r + mov_r < N and 0 <= c + mov_c < M and Map[r + mov_r][c + mov_c] == 0):
            count += 1
            move(r + mov_r, c + mov_c, d)
    else:
        d = 3
        mov_r, mov_c = dir(d)
        if (0 <= r + mov_r < N and 0 <= c + mov_c < M and Map[r + mov_r][c + mov_c] == 0):
            count += 1
            move(r + mov_r, c + mov_c, d)
move(loc_r , loc_c, d)
print(count)
