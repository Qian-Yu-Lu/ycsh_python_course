
n = input('第一個數字')
m = input('第二個數字')
n = int(n)
m = int(m)

if n < m:
    pass
else:
    n, m = m, n

for i in range(n + 1, m):
    for j in range(1, i):
        if i % j == 0 and j != 1:
            break
        if j == i - 1:
print()