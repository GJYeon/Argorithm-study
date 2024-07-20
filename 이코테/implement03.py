loc = input()
loc_x = loc[0]
loc_y =int(loc[1])
m = ['a','b','c','d','e','f','g','h']
for i in range(len(m)):
    if (loc_x == m[i]):
        loc_xtoint = i+1

mov = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
count = 0
for j,k in mov:
    j += loc_xtoint
    k += loc_y
    if(0<j and j<9 and 0<k and k <9):
        count += 1

print(count)

