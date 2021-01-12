x = int(input("請輸入月份："))
if x >= 2 and x <= 4:
    print("春天")
elif x >= 5 and x <= 7:
    print("夏天")
elif x >= 8 and x <= 10:
    print("秋天")
elif x ==11 or x == 12 or x == 1 :
    print("冬天")
else:
    print("輸入錯誤")