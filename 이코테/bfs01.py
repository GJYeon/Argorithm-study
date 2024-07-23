from collections import deque

N, M = map(int, input().split())
Map = list()
for i in range(N):
    Map.append(input())
visited = [[0]*M for _ in range(N)]
queue = deque()
dx = [-1,0,1,0]
dy = [0,-1,0,1]
count = 0
for i in range(N):
    for j in range(M):
        if(Map[i][j]=='0' and visited[i][j] == 0 ):
            visited[i][j] = 1
            queue.append((i,j))
            while(queue):
                n,m = queue.popleft()
                for k in range(4):
                    y = n+dy[k]
                    x = m+dx[k]
                    if(0<=y<N and 0<=x<M and Map[y][x] == '0' and visited[y][x]==0):
                        visited[y][x] = 1
                        queue.append((y,x))
            count += 1
print(count)

'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''