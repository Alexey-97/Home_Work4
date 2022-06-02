def cutString(
    word  = input("""Введите текст:
""")):
    word = word.split()
    count = 0
    s = []

    for i in word:
        for j in i:
            count += 1
        if count > 10:
            s.append(i[:7]+"...")
        else:
            s.append(i)
        count = 0
    print(" ".join(s))
    return        
       
