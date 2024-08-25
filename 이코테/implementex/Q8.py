#문자열이 주어졌을때 알파벳 타입과 숫자 타입을 구분하기
S = input()
alphasave = list()
digitsave = list()
for i in S:
    if(i.isalpha()):
        alphasave.append(i)
    else:
        digitsave.append(i)
alphasave.sort()
sum = 0
for i in digitsave:
    sum += int(i)
result = ''
for i in alphasave:
    result += i
result += str(sum)
print(result)