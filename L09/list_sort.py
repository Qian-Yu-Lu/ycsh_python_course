y = []

for i in range(5):
    x =  x = int(input('請輸入第'+ str(i+1)+'個數字'))
    y.append(x)
    y.sort()
    y.reverse()
print(y)