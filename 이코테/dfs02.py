from collections import deque
#DFS, BFS에서 최소 칸의 개수 이런거 나오면 거리정보도 좌표와 같이 묶는다.  ex-> (x,y,거리) 이런식으로
N,M = map(int, input().split())
Map = list()
visited = [[0]*M for _ in range(N)]
for _ in range(N):
    Map.append(input())
x = 0
y = 0
dx = [-1,0,1,0]
dy = [0,-1,0,1]
distance = 1
queue = deque()
queue.append((y,x,distance))
while(queue):
    y,x,d = queue.popleft()
    if(y==N-1 and x == M-1):
        break
    d += 1
    for i in range(4):
        n = y + dy[i]
        m = x + dx[i]
        if(0<=n<N and 0<=m<M and visited[n][m] == 0 and Map[n][m] == '1'):
            queue.append((n,m,d))
distance = d
print(distance)