num = int(input())
num = str(num)
result = int(num[0])
for i in range(1,len(num)):
    if num[i] == '0' or num[i] == '1':
        result += int(num[i])
    else:
        result *= int(num[i])
print(result)