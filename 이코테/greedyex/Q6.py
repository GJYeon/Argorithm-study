#먹을 순서가 정해졌을때 k초에 방송 중단시 먹어야 하는 음식 구하기
def solution(food_times, k):
    answer = 0
    i = 0
    count = 0
    while(True):
        if(food_times[i] == 0):
            continue
        if(count==k):
            answer = i
            break
        food_times[i] -= 1
        i += 1
        if(i >= len(food_times)):
            i = 0
        count += 1
    return answer