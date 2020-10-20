h = float (input("請輸入身高"))
w = float (input("請輸入身高"))

h = h/100.0
bmi = w/h**2
bmi = round(bmi,2)
print("身高:",h)
print("體重:",w)
print("BMI:",bmi)
