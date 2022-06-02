def divider_max_min(m,n):
    if m > n:  
        temp = m 
    else: 
        temp = n 
    for i in range(1, temp + 1): 
        if(( m % i == 0) and(n % i == 0 )): 
            gcd = i
    print("НОД = ",gcd)
    if m > n:
        greater = m
    else:
        greater = n 
    while(True): 
        if((greater % m == 0) and (greater % n == 0)): 
            lcm = greater
            break 
        greater += 1
    print("НОК = ",greater)
    return

     


