lst1 = [9]

lst1 = map(str, lst1)
lst_to_str = str()

for i in lst1:
    lst_to_str += i
lst_to_str = list(tuple(str(int(lst_to_str) + 1)))

for i, el in enumerate(lst_to_str):
    lst_to_str[i] = int(el)
print(lst_to_str)