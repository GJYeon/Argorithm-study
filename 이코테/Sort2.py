N = int(input())
array = list()
for _ in range(N):
    name, score = input().split()
    array.append((name, int(score)))

array.sort(key = lambda x: x[1])
for i in array:
    print(i[0],end=' ')