txt = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0,
       9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
print(txt)

lst = list()
count = 0

for i in range(len(txt)):
    if (txt[i] == 0):
        count += 1

    else:
        lst.append(txt[i])
lst.extend([0] * count)
print(lst)