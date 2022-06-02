def equations(F,x):
    if F == 1:
        if x <= 3:
            a =  x ** 2 - 3 * x + 9
            print (a)
        else:
            a = 1 / (x ** 3 + 6)
            print(a)
    elif F == 2:
        if x <= 2:
            b =  x ** 2 + 4 * x + 5
            print (b)
        else:
            b = 1 / (x ** 2 + 4 * x + 5)
            print(b)
    elif F == 3:
        if x > 3:
            c =  -3 * x + 9
            print (c)
        else:
            c = x ** 3 / (x ** 2 + 8)
            print(c)
        return