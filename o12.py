i = 1
while i <= 4000:
    if(i % 11 == 0) and (i % 9 == 0) and (i % 3 == 0):
        print(i, end='  ')
    i += 1