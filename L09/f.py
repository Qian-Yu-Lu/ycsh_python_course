y = [0,1]

x = int(input())
for n in range(2,x+1):
    F = y[n-1]+y[n-2]
    y.append(F)
print(y[x])