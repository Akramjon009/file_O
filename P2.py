lis = [2, 34, 56, 78, 8, 98]
lis2 = lis.copy()
print(lis)
for i in range(len(lis)):
    if i % 2:
       lis2[i] = pow(lis[i], 3)
    else:
        lis2[i] = pow(lis[i], 2)

print(lis2)
