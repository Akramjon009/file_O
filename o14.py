m = int(input())
n = 0
if m > 0:
    for i in range(m+1):
        n += i
else:
    for i in range(1, m - 1, -1):
        n += i
print(n)