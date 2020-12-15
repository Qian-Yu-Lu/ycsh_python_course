
x = int(input("請輸入數字"))
for i in range(2, x):
    if x % i == 0:
        print("不是質數")
        break
else:
    print("是質數")