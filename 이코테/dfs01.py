#DFS문제는 스택을 이용한다

N,M = map(int,input().split())
Map = list()
for i in range(N):
    Map.append(input())

dx = [-1,0,1,0]
dy = [0,-1,0,1]
search_map = [[0]*M for _ in range(N)] #[[0]*M]*N 이렇게 쓰면 [0]*M의 복사본이 N개 생성
search_stack = list()
count = 0
for i in range(N):
    for j in range(M):
        if(Map[i][j]=='0' and search_map[i][j]==0):
            search_map[i][j] = 1
            search_stack.append((i,j))
            while(search_stack):
                loc = search_stack.pop()
                for k in range(4):
                    y = loc[0]+dy[k]
                    x = loc[1]+dx[k]
                    if(0<=y<N and 0<=x<M and Map[y][x]=='0' and search_map[y][x]==0):
                        search_map[y][x] = 1
                        search_stack.append((y,x))
            count += 1

print(count)