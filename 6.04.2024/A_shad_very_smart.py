n = int(input())
a = list(map(int, input().split()))
can, p = a[0], 1
for i in range(1, n):
    if a[i] == can:
        p += 1
    elif p == 0 or (can < a[i] and p == 1):
        can = a[i]
        p += 1
    else:
        p -= 1

print(can)