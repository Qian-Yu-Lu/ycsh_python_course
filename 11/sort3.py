a = int(input('請輸入數字:'))
b = int(input('請輸入數字:'))
c = int(input('請輸入數字:'))
if a > b and b > c:
    x = a
    y = b
    z = c
elif a > c and c > b:
    x = a
    y = c
    z = b
elif b > c and c > a:
    x = b
    y = c
    z = a
elif b > a and a > c:
    x = b
    y = a
    z = c
elif c > a and a > b:
    x = c
    y = a
    z = b
elif c > b and b > a:
    x = c
    y = b
    z = a


print(x)
print(y)
print(z)