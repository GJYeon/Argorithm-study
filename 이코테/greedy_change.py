changemoney = int(input()) #거스름돈
change500, change100, change50, change10 = 0,0,0,0
change500 = changemoney // 500
change100 = (changemoney % 500) // 100
change50 = (changemoney % 100) // 50
change10 = (changemoney % 50) // 10

count = change500 + change100 + change50 + change10 #거스름돈 동전 개수 세기

print(count)

#거스름돈 문제에서 동전의 단위가 서로 배수 형태가 아니라 무작위로 주어진 경우에는 그리디 알고리즘으로 해결할 수 없다.
