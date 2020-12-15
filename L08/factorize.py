x = 12

while x > 1:
    for i in range( 2, x+1 ):
        if x % i== 0:
            print(i)
            break

    x = x // i