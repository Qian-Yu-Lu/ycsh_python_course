a = int(input('請輸入數字:'))
b = int(input('請輸入數字:'))
c = int(input('請輸入數字:'))
d = int(input('請輸入數字:'))
e = int(input('請輸入數字:'))
f = int(input('請輸入數字:'))
i = 0

while i < 6:

    if f > e :
        f,e = e,f
    elif e > d :
        e,d = d,e
    elif c > d :
        c,d = d,c
    elif b> c :
        b,c = c,b
    elif a > b:
        a,b = b,a 
i = i + 1

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)